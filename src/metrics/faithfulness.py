import re
from typing import List
from openai import OpenAI
from ..utils import extract_json_from_response, clean_statement_numbering

class FaithfulnessMetric:
    """
    Faithfulness Metric: Ratio of statements supported by the context
    According to Section 3 of the RAGAs paper
    """
    def __init__(self, client: OpenAI, model: str = "gpt-4o"):
        self.client = client
        self.model = model

    def extract_statements(self, question: str, answer: str) -> List[str]:
        """
        Step 1: Extract statements from the answer
        Prompt: "Given a question and answer, create one or more statements from each sentence..."
        """
        prompt = f"""Given a question and answer, create one or more statements from each sentence in the given answer.
Question: {question}
Answer: {answer}

Output each statement on a new line, numbered. Do not add any extra text.
Statements:
"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        content = response.choices[0].message.content.strip()
        lines = content.split('\n')
        statements = []
        for line in lines:
            cleaned = clean_statement_numbering(line)
            if cleaned:
                statements.append(cleaned)
        return statements

    def verify_statement(self, statement: str, context: str) -> bool:
        """
        Step 2: Check whether a statement can be inferred from the context
        Prompt with JSON output for more accuracy
        """
        prompt = f"""Consider the given context and following statement, then determine whether it is supported by the information present in the context.
Provide a brief explanation before arriving at the verdict (Yes/No).
At the end, output the verdict in JSON format: {{"verdict": "Yes"}} or {{"verdict": "No"}}.

Context: {context}
Statement: {statement}
"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        content = response.choices[0].message.content
        verdict_json = extract_json_from_response(content)
        if verdict_json and "verdict" in verdict_json:
            return verdict_json["verdict"].lower() == "yes"
        # Fallback: search for Yes/No word
        return "yes" in content.lower()

    def compute(self, question: str, answer: str, context: str) -> float:
        """Faithfulness score = number of supported statements / total number of statements"""
        statements = self.extract_statements(question, answer)
        if not statements:
            return 0.0
        supported = sum(1 for stmt in statements if self.verify_statement(stmt, context))
        return supported / len(statements)