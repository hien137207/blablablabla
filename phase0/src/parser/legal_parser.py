import re
import json
import os
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional

@dataclass
class Chunk:
    chunk_id: str
    document_id: str
    document_title: str
    domain: str
    article: Optional[str] = None
    clause: Optional[str] = None
    point: Optional[str] = None
    chapter: Optional[str] = None
    content: str = ""
    chunk_index: int = 0

@dataclass
class ParsedDocument:
    document_id: str
    title: str
    domain: str
    file_path: str
    chapters: list = field(default_factory=list)
    articles: list = field(default_factory=list)
    chunks: list = field(default_factory=list)
    raw_text: str = ""

class LegalDocumentParser:
    """
    Parses Vietnamese legal documents into a structured hierarchy:
    Document -> Chapter -> Article -> Clause -> Point

    Vietnamese legal structure patterns:
    - CHƯƠNG I, CHƯƠNG II, etc. (Chapter headers)
    - Điều 1., Điều 12. (Article headers)
    - 1., 2., 3. (Clause numbers)
    - a), b), c) (Point letters)
    """

    CHAPTER_PATTERN = re.compile(r'^CHƯƠNG\s+([IVXLC]+)\s*$')
    ARTICLE_PATTERN = re.compile(r'^Điều\s+(\d+)\.\s*(.*)')
    CLAUSE_PATTERN = re.compile(r'^(\d+)\.\s+(.*)')
    POINT_PATTERN = re.compile(r'^([a-z])\)\s+(.*)')

    def __init__(self):
        self.documents = []

    def parse_file(self, file_path: str, domain: str) -> ParsedDocument:
        path = Path(file_path)
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

        document_id = path.stem
        title = self._extract_title(text)

        doc = ParsedDocument(
            document_id=document_id,
            title=title,
            domain=domain,
            file_path=str(path),
            raw_text=text
        )

        lines = text.split('\n')
        self._parse_structure(lines, doc)
        self._generate_chunks(doc)

        self.documents.append(doc)
        return doc

    def _extract_title(self, text: str) -> str:
        lines = text.strip().split('\n')
        for line in lines[:5]:
            line = line.strip()
            if line and not line.startswith('(') and len(line) > 5:
                return line
        return "Untitled"

    def _parse_structure(self, lines: list, doc: ParsedDocument):
        current_chapter = None
        current_article = None
        current_clause = None
        buffer = []

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue

            chap_match = self.CHAPTER_PATTERN.match(stripped)
            art_match = self.ARTICLE_PATTERN.match(stripped)
            clause_match = self.CLAUSE_PATTERN.match(stripped)
            point_match = self.POINT_PATTERN.match(stripped)

            if chap_match:
                if buffer and current_article:
                    current_article['full_text'] = '\n'.join(buffer).strip()
                current_chapter = {
                    'number': chap_match.group(1),
                    'title': '',
                    'articles': []
                }
                doc.chapters.append(current_chapter)
                buffer = []
            elif art_match:
                if buffer and current_article:
                    current_article['full_text'] = '\n'.join(buffer).strip()
                current_article = {
                    'number': art_match.group(1),
                    'title': art_match.group(2).strip(),
                    'clauses': [],
                    'full_text': ''
                }
                doc.articles.append(current_article)
                if current_chapter:
                    current_chapter['articles'].append(current_article)
                buffer = [stripped]
            elif clause_match and current_article:
                current_clause = {
                    'number': clause_match.group(1),
                    'content': clause_match.group(2).strip(),
                    'points': []
                }
                current_article['clauses'].append(current_clause)
                buffer = [stripped]
            elif point_match and current_article and current_article['clauses']:
                point = {
                    'letter': point_match.group(1),
                    'content': point_match.group(2).strip()
                }
                current_article['clauses'][-1]['points'].append(point)
                buffer.append(stripped)
            else:
                if current_article:
                    buffer.append(stripped)

        if buffer and current_article:
            current_article['full_text'] = '\n'.join(buffer).strip()

    def _generate_chunks(self, doc: ParsedDocument):
        chunk_index = 0

        for article in doc.articles:
            article_chunk = Chunk(
                chunk_id=f"{doc.document_id}_art{article['number']}",
                document_id=doc.document_id,
                document_title=doc.title,
                domain=doc.domain,
                article=article['number'],
                chapter=self._find_chapter_for_article(doc, article['number']),
                content=article.get('full_text', ''),
                chunk_index=chunk_index
            )
            doc.chunks.append(article_chunk)
            chunk_index += 1

            for clause in article.get('clauses', []):
                clause_content = clause['content']
                if clause.get('points'):
                    points_text = '\n'.join(
                        f"  {p['letter']}) {p['content']}" for p in clause['points']
                    )
                    clause_content = f"{clause_content}\n{points_text}"

                clause_chunk = Chunk(
                    chunk_id=f"{doc.document_id}_art{article['number']}_k{clause['number']}",
                    document_id=doc.document_id,
                    document_title=doc.title,
                    domain=doc.domain,
                    article=article['number'],
                    clause=clause['number'],
                    chapter=self._find_chapter_for_article(doc, article['number']),
                    content=clause_content,
                    chunk_index=chunk_index
                )
                doc.chunks.append(clause_chunk)
                chunk_index += 1

    def _find_chapter_for_article(self, doc: ParsedDocument, article_num: str) -> Optional[str]:
        for chapter in doc.chapters:
            for art in chapter['articles']:
                if art['number'] == article_num:
                    return chapter['number']
        return None

    def parse_directory(self, dir_path: str, domain: str) -> list:
        docs = []
        path = Path(dir_path)
        for filepath in sorted(path.glob('*.txt')):
            doc = self.parse_file(str(filepath), domain)
            docs.append(doc)
        return docs

    def get_all_chunks(self) -> list:
        chunks = []
        for doc in self.documents:
            chunks.extend(doc.chunks)
        return chunks

    def export_chunks_json(self, output_path: str):
        chunks_data = []
        for doc in self.documents:
            for chunk in doc.chunks:
                chunks_data.append(asdict(chunk))
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(chunks_data, f, ensure_ascii=False, indent=2)
        return len(chunks_data)
