import numpy as np
from typing import List
from openai import OpenAI

class AnswerRelevancyMetric:
    """
    Answer Relevancy Metric: Average cosine similarity between the original question 
    and questions generated from the answer
    According to Section 3 of the RAGAs paper (Equation 1)
    """
    def __init__(self, client: OpenAI, llm_model: str = "gpt-4o", embedding_model: str = "text-embedding-3-small"):
        self.client = client
        self.llm_model = llm_model
        self.embedding_model = embedding_model

    def _get_embedding(self, text: str) -> np.ndarray:
        """Get embedding vector from gapgpt API (OpenAI compatible)"""
        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=text
        )
        embedding = response.data[0].embedding
        return np.array(embedding, dtype=np.float32)

    def _cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        """Cosine similarity between two vectors"""
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8))

    def _generate_questions(self, answer: str, n: int = 3) -> List[str]:
        """
        Generate n questions from the answer (inverse question generation)
        Simple prompt according to the paper: "Generate a question for the given answer."
        """
        prompt = f"""Generate exactly {n} different questions that could be answered by the following answer. 
Output each question on a new line. Do not number them.

Answer: {answer}
Questions:
"""
        response = self.client.chat.completions.create(
            model=self.llm_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        content = response.choices[0].message.content.strip()
        lines = [line.strip() for line in content.split('\n') if line.strip() and not line.lower().startswith("questions")]
        # Sometimes the model may generate fewer than n questions
        return lines[:n] if lines else []

    def compute(self, question: str, answer: str, n: int = 3) -> float:
        """
        AR = (1/n) * sum(cosine_sim(embed(question), embed(q_i)))
        """
        generated_qs = self._generate_questions(answer, n)
        if not generated_qs:
            return 0.0
        q_emb = self._get_embedding(question)
        similarities = []
        for gq in generated_qs:
            gq_emb = self._get_embedding(gq)
            similarities.append(self._cosine_similarity(q_emb, gq_emb))
        return float(np.mean(similarities))