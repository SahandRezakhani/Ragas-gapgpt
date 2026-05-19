from typing import List
from openai import OpenAI
from ..utils import split_sentences

class ContextRelevancyMetric:
    """
    Context Relevancy Metric: Ratio of relevant sentences to total context sentences
    According to Section 3 of the RAGAs paper (Equation 2)
    """
    def __init__(self, client: OpenAI, model: str = "gpt-4o"):
        self.client = client
        self.model = model

    def _extract_relevant_sentences(self, question: str, context: str) -> List[str]:
        """
        Extract sentences from the context that are essential for answering the question
        Prompt exactly according to the paper
        """
        prompt = f"""Please extract relevant sentences from the provided context that can potentially help answer the following question. 
If no relevant sentences are found, or if you believe the question cannot be answered from the given context, return the phrase "Insufficient Information". 
While extracting candidate sentences you're not allowed to make any changes to sentences from given context. 
Output each extracted sentence on a new line, exactly as they appear in the context.

Question: {question}
Context: {context}

Relevant sentences:
"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        content = response.choices[0].message.content.strip()
        if "Insufficient Information" in content:
            return []
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        return lines

    def compute(self, question: str, context: str) -> float:
        """
        CR = (number of extracted sentences) / (total number of sentences in context)
        """
        all_sentences = split_sentences(context)
        total = len(all_sentences)
        if total == 0:
            return 0.0
        relevant_sentences = self._extract_relevant_sentences(question, context)
        unique_relevant = set(relevant_sentences)
        return len(unique_relevant) / total