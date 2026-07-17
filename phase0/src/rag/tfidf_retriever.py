import json
import math
import re
from dataclasses import dataclass, asdict
from typing import Optional
from collections import Counter

@dataclass
class RetrievalResult:
    chunk_id: str
    document_id: str
    document_title: str
    article: Optional[str]
    clause: Optional[str]
    content: str
    score: float
    rank: int

class VietnameseTokenizer:
    """
    Lightweight Vietnamese tokenizer for the Phase 0 experiment.
    Splits on whitespace and punctuation, normalizes diacritics.
    For production, this would be replaced with a proper Vietnamese
    word segmenter (e.g., underthesea or VnCoreNLP).
    """

    STOPWORDS = {
        'của', 'và', 'là', 'trong', 'được', 'có', 'không', 'với', 'cho',
        'từ', 'theo', 'để', 'khi', 'các', 'một', 'hoặc', 'phải', 'người',
        'này', 'đó', 'những', 'về', 'tại', 'bị', 'bằng', 'trên', 'dưới',
        'cũng', 'sẽ', 'đã', 'còn', 'nếu', 'thì', 'mà', 'lên', 'xuống',
        'ra', 'vào', 'lại', 'đi', 'đến', 'nên', 'vẫn', 'chỉ', 'như',
        'a', 'b', 'c', 'd', 'đ', 'e', 'g', 'h', 'i', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y'
    }

    def tokenize(self, text: str) -> list:
        text = text.lower()
        text = re.sub(r'[^\w\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', ' ', text)
        tokens = text.split()
        return [t for t in tokens if t and t not in self.STOPWORDS and len(t) > 1]


class TFIDFRetriever:
    """
    Lightweight TF-IDF retrieval for Phase 0 RAG baseline.
    Simulates vector search + keyword matching without external dependencies.

    Architecture mapping:
    - TF-IDF vectors simulate Qdrant vector search
    - Term overlap simulates BM25 keyword search
    - Combined score represents hybrid retrieval
    """

    def __init__(self, chunks: list):
        self.chunks = chunks
        self.tokenizer = VietnameseTokenizer()
        self.tokenized_chunks = [self.tokenizer.tokenize(c['content']) for c in chunks]
        self._build_index()

    def _build_index(self):
        self.df = Counter()
        for tokens in self.tokenized_chunks:
            unique_terms = set(tokens)
            for term in unique_terms:
                self.df[term] += 1

        self.N = len(self.tokenized_chunks)
        self.idf = {}
        for term, df in self.df.items():
            self.idf[term] = math.log((self.N + 1) / (df + 1)) + 1

        self.tf_idf_vectors = []
        for tokens in self.tokenized_chunks:
            tf = Counter(tokens)
            vec = {}
            for term, count in tf.items():
                vec[term] = count * self.idf.get(term, 0)
            self.tf_idf_vectors.append(vec)

    def _cosine_similarity(self, vec_a: dict, vec_b: dict) -> float:
        if not vec_a or not vec_b:
            return 0.0
        dot = sum(vec_a.get(t, 0) * vec_b.get(t, 0) for t in vec_a)
        mag_a = math.sqrt(sum(v ** 2 for v in vec_a.values()))
        mag_b = math.sqrt(sum(v ** 2 for v in vec_b.values()))
        if mag_a == 0 or mag_b == 0:
            return 0.0
        return dot / (mag_a * mag_b)

    def _keyword_overlap_score(self, query_tokens: list, chunk_tokens: list) -> float:
        query_set = set(query_tokens)
        chunk_set = set(chunk_tokens)
        if not query_set:
            return 0.0
        overlap = query_set & chunk_set
        return len(overlap) / len(query_set)

    def _article_match_bonus(self, query: str, chunk: dict) -> float:
        """
        Legal structure relevance: if the query mentions a specific article number
        and the chunk belongs to that article, give a bonus.
        """
        article_nums = re.findall(r'điều\s+(\d+)', query.lower())
        if not article_nums:
            return 0.0
        chunk_article = str(chunk.get('article', ''))
        for num in article_nums:
            if num == chunk_article:
                return 0.3
        return 0.0

    def retrieve(self, query: str, top_k: int = 5) -> list:
        query_tokens = self.tokenizer.tokenize(query)
        query_tf = Counter(query_tokens)
        query_vec = {}
        for term, count in query_tf.items():
            query_vec[term] = count * self.idf.get(term, math.log(self.N + 1))

        results = []
        for i, chunk in enumerate(self.chunks):
            vector_score = self._cosine_similarity(query_vec, self.tf_idf_vectors[i])
            keyword_score = self._keyword_overlap_score(query_tokens, self.tokenized_chunks[i])
            article_bonus = self._article_match_bonus(query, chunk)

            hybrid_score = (0.5 * vector_score) + (0.3 * keyword_score) + (0.2 * article_bonus)

            results.append(RetrievalResult(
                chunk_id=chunk['chunk_id'],
                document_id=chunk['document_id'],
                document_title=chunk['document_title'],
                article=chunk.get('article'),
                clause=chunk.get('clause'),
                content=chunk['content'][:200],
                score=hybrid_score,
                rank=0
            ))

        results.sort(key=lambda x: x.score, reverse=True)
        for rank, result in enumerate(results[:top_k]):
            result.rank = rank + 1

        return results[:top_k]

    def evaluate_retrieval(self, evaluation_questions: list, top_k: int = 5) -> dict:
        """
        Evaluate retrieval accuracy against the evaluation dataset.
        A retrieval is correct if the expected document + article appears in top-K.
        """
        correct = 0
        total = len(evaluation_questions)
        per_question_results = []

        for q in evaluation_questions:
            results = self.retrieve(q['question'], top_k=top_k)
            expected_doc = q['expected_evidence']['document'].replace('.txt', '')
            expected_article = q['expected_evidence']['article']

            found = False
            for r in results:
                if r.document_id == expected_doc and str(r.article) == str(expected_article):
                    found = True
                    break

            if found:
                correct += 1

            per_question_results.append({
                'question_id': q['id'],
                'question': q['question'],
                'expected_doc': expected_doc,
                'expected_article': expected_article,
                'retrieved': [
                    {
                        'chunk_id': r.chunk_id,
                        'document_id': r.document_id,
                        'article': r.article,
                        'clause': r.clause,
                        'score': round(r.score, 4)
                    } for r in results
                ],
                'correct': found
            })

        accuracy = correct / total if total > 0 else 0
        return {
            'accuracy': accuracy,
            'correct': correct,
            'total': total,
            'target_accuracy': 0.85,
            'meets_target': accuracy >= 0.85,
            'per_question': per_question_results
        }
