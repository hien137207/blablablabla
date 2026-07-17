import re
import json
from dataclasses import dataclass, asdict
from typing import Optional
from enum import Enum

class ValidationStatus(Enum):
    APPROVED = "approved"
    REJECTED_INVALID_REFERENCE = "rejected_invalid_reference"
    REJECTED_NO_EVIDENCE = "rejected_no_evidence"
    REJECTED_MISALIGNED = "rejected_misaligned"

@dataclass
class Citation:
    document_id: str
    document_title: str
    article: Optional[str] = None
    clause: Optional[str] = None
    chunk_id: Optional[str] = None

@dataclass
class ValidationResult:
    citation: Citation
    status: ValidationStatus
    reason: str
    document_exists: bool = False
    article_exists: bool = False
    evidence_aligned: bool = False

    def to_dict(self) -> dict:
        return {
            'citation': asdict(self.citation),
            'status': self.status.value,
            'reason': self.reason,
            'document_exists': self.document_exists,
            'article_exists': self.article_exists,
            'evidence_aligned': self.evidence_aligned,
        }

class CitationValidator:
    """
    Citation validation prototype implementing the architecture spec:
    1. Check Document Exists
    2. Check Article Exists
    3. Compare Evidence Alignment
    4. Approve / Reject

    On validation failure, the system should attempt regeneration once,
    then return the uncertainty response.
    """

    CITATION_PATTERNS = [
        re.compile(r'Điều\s+(\d+)', re.IGNORECASE),
        re.compile(r'khoản\s+(\d+)', re.IGNORECASE),
        re.compile(r'Nghị định\s+ số\s+(\d+)/(\d+)/NĐ-CP', re.IGNORECASE),
        re.compile(r'Luật\s+Lao\s+động\s*(\d*)', re.IGNORECASE),
        re.compile(r'Luật\s+Xử\s+phạt', re.IGNORECASE),
        re.compile(r'Nghị định\s+(\d+)/(\d+)/NĐ-CP', re.IGNORECASE),
    ]

    UNCERTAINTY_RESPONSE = "Không đủ căn cứ pháp lý để đưa ra kết luận."

    def __init__(self, chunks: list):
        self.chunks = chunks
        self.documents = {}
        self.articles_by_doc = {}

        for chunk in chunks:
            doc_id = chunk['document_id']
            if doc_id not in self.documents:
                self.documents[doc_id] = {
                    'id': doc_id,
                    'title': chunk['document_title'],
                    'domain': chunk['domain'],
                    'articles': set()
                }
            if chunk.get('article'):
                self.documents[doc_id]['articles'].add(str(chunk['article']))

        for doc_id, doc_info in self.documents.items():
            self.articles_by_doc[doc_id] = doc_info['articles']

    def extract_citations_from_text(self, text: str) -> list:
        """Extract citation references from generated answer text.

        Two-pass approach: first detect document references, then article
        references, then merge them into unified Citation objects.
        """
        doc_ids = set()

        nd_matches = re.findall(r'Nghị định\s+số\s+(\d+)/(\d+)/NĐ-CP', text, re.IGNORECASE)
        nd_matches += re.findall(r'Nghị định\s+(\d+)/(\d+)/NĐ-CP', text, re.IGNORECASE)
        for nd_num, year in nd_matches:
            if nd_num == '100' and year == '2019':
                doc_ids.add('nghi_dinh_100_2019_xu_phat_giao_thong')
            elif nd_num == '123' and year == '2021':
                doc_ids.add('nghi_dinh_123_2021_sua_doi_nghi_dinh_100')

        ld_matches = re.findall(r'Luật\s+Lao\s+động\s*(\d*)', text, re.IGNORECASE)
        for year in ld_matches:
            if year == '2012':
                doc_ids.add('bo_luat_lao_dong_2012')
            elif year == '2019' or year == '':
                doc_ids.add('luat_lao_dong_2019')

        if re.search(r'Luật\s+Xử\s+phạt', text, re.IGNORECASE):
            doc_ids.add('luat_xuat_giao_thong_duong_bo_2024')

        article_nums = re.findall(r'Điều\s+(\d+)', text, re.IGNORECASE)
        clause_nums = re.findall(r'khoản\s+(\d+)', text, re.IGNORECASE)

        citations = []
        seen = set()

        doc_list = sorted(doc_ids) if doc_ids else [None]
        art_list = article_nums if article_nums else [None]

        for doc_id in doc_list:
            for art_num in art_list:
                key = (doc_id, art_num)
                if key in seen:
                    continue
                seen.add(key)

                doc_title = self.documents.get(doc_id, {}).get('title', 'Unknown') if doc_id else 'Unknown'

                citations.append(Citation(
                    document_id=doc_id or 'unknown',
                    document_title=doc_title,
                    article=art_num,
                    clause=clause_nums[0] if clause_nums else None
                ))

        return citations

    def validate_citation(self, citation: Citation, answer_text: str, retrieved_evidence: list) -> ValidationResult:
        """
        Validate a single citation through the full pipeline:
        1. Document exists?
        2. Article exists in document?
        3. Evidence alignment?
        """
        doc_exists = citation.document_id in self.documents

        if not doc_exists:
            return ValidationResult(
                citation=citation,
                status=ValidationStatus.REJECTED_INVALID_REFERENCE,
                reason=f"Document '{citation.document_id}' does not exist in the corpus.",
                document_exists=False,
                article_exists=False,
                evidence_aligned=False
            )

        article_exists = True
        if citation.article:
            article_str = str(citation.article)
            article_exists = article_str in self.articles_by_doc.get(citation.document_id, set())

        if not article_exists:
            return ValidationResult(
                citation=citation,
                status=ValidationStatus.REJECTED_INVALID_REFERENCE,
                reason=f"Article {citation.article} does not exist in document '{citation.document_id}'.",
                document_exists=True,
                article_exists=False,
                evidence_aligned=False
            )

        evidence_aligned = self._check_evidence_alignment(citation, answer_text, retrieved_evidence)

        if not evidence_aligned:
            return ValidationResult(
                citation=citation,
                status=ValidationStatus.REJECTED_MISALIGNED,
                reason="Cited evidence does not align with retrieved evidence.",
                document_exists=True,
                article_exists=True,
                evidence_aligned=False
            )

        return ValidationResult(
            citation=citation,
            status=ValidationStatus.APPROVED,
            reason="Citation validated: document exists, article exists, evidence aligns.",
            document_exists=True,
            article_exists=True,
            evidence_aligned=True
        )

    def _check_evidence_alignment(self, citation: Citation, answer_text: str, retrieved_evidence: list) -> bool:
        """
        Check if the cited document+article appears in the retrieved evidence.
        This simulates verifying that the answer is grounded in retrieved context.
        """
        for evidence in retrieved_evidence:
            if (evidence.get('document_id') == citation.document_id and
                str(evidence.get('article', '')) == str(citation.article)):
                return True
        return False

    def validate_answer(self, answer_text: str, retrieved_evidence: list) -> dict:
        """
        Full validation flow for a generated answer.
        Returns the validation results and whether the answer is safe to display.
        """
        citations = self.extract_citations_from_text(answer_text)

        if not citations:
            return {
                'valid': False,
                'should_display': False,
                'fallback_response': self.UNCERTAINTY_RESPONSE,
                'reason': 'No citations found in answer.',
                'citations': []
            }

        results = []
        all_valid = True

        for citation in citations:
            result = self.validate_citation(citation, answer_text, retrieved_evidence)
            results.append({
                'citation': asdict(citation),
                'status': result.status.value,
                'reason': result.reason,
                'document_exists': result.document_exists,
                'article_exists': result.article_exists,
                'evidence_aligned': result.evidence_aligned
            })
            if result.status != ValidationStatus.APPROVED:
                all_valid = False

        return {
            'valid': all_valid,
            'should_display': all_valid,
            'fallback_response': self.UNCERTAINTY_RESPONSE if not all_valid else None,
            'reason': 'All citations validated.' if all_valid else 'One or more citations failed validation.',
            'citations': results
        }

    def test_valid_citation(self, chunks: list) -> dict:
        """Test case: valid citation referencing existing article."""
        citation = Citation(
            document_id='luat_xuat_giao_thong_duong_bo_2024',
            document_title='LUẬT XỬ PHẠT HÀNH CHÍNH TRONG LĨNH VỰC GIAO THÔNG ĐƯỜNG BỘ',
            article='10',
            clause='1'
        )
        evidence = [{'document_id': 'luat_xuat_giao_thong_duong_bo_2024', 'article': '10'}]
        result = self.validate_citation(citation, "Theo Điều 10...", evidence)
        return {'test': 'valid_citation', 'result': result.to_dict()}

    def test_invalid_article(self, chunks: list) -> dict:
        """Test case: citation referencing non-existent article."""
        citation = Citation(
            document_id='luat_xuat_giao_thong_duong_bo_2024',
            document_title='LUẬT XỬ PHẠT HÀNH CHÍNH',
            article='999',
            clause='1'
        )
        evidence = []
        result = self.validate_citation(citation, "Theo Điều 999...", evidence)
        return {'test': 'invalid_article', 'result': result.to_dict()}

    def test_invalid_document(self, chunks: list) -> dict:
        """Test case: citation referencing non-existent document."""
        citation = Citation(
            document_id='fake_law_2024',
            document_title='Fake Law',
            article='1',
            clause='1'
        )
        evidence = []
        result = self.validate_citation(citation, "Theo luật giả...", evidence)
        return {'test': 'invalid_document', 'result': result.to_dict()}

    def test_no_evidence_alignment(self, chunks: list) -> dict:
        """Test case: citation exists but evidence doesn't align."""
        citation = Citation(
            document_id='luat_xuat_giao_thong_duong_bo_2024',
            document_title='LUẬT XỬ PHẠT',
            article='10',
            clause='1'
        )
        evidence = [{'document_id': 'luat_lao_dong_2019', 'article': '20'}]
        result = self.validate_citation(citation, "Theo Điều 10...", evidence)
        return {'test': 'no_evidence_alignment', 'result': result.to_dict()}

    def test_fabricated_answer(self, chunks: list) -> dict:
        """Test case: answer with fabricated citations."""
        fake_answer = "Theo Điều 999 của Nghị định số 500/2099/NĐ-CP, phạt 50 triệu đồng."
        evidence = [{'document_id': 'luat_xuat_giao_thong_duong_bo_2024', 'article': '10'}]
        result = self.validate_answer(fake_answer, evidence)
        return {'test': 'fabricated_answer', 'result': result}

    def test_well_grounded_answer(self, chunks: list) -> dict:
        """Test case: well-grounded answer with valid citations."""
        good_answer = "Theo Điều 10 của Luật Xử phạt, không đội mũ bảo hiểm bị phạt từ 200.000 đồng đến 300.000 đồng."
        evidence = [{'document_id': 'luat_xuat_giao_thong_duong_bo_2024', 'article': '10'}]
        result = self.validate_answer(good_answer, evidence)
        return {'test': 'well_grounded_answer', 'result': result}
