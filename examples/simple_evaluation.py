import os
from dotenv import load_dotenv
from src.evaluator import RAGASEvaluator

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv("GAPGPT_API_KEY")
BASE_URL = os.getenv("GAPGPT_BASE_URL", "https://api.gapgpt.app/v1")
MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

# Sample question, context, and answers (taken from the paper)
question = "Who directed the film Oppenheimer and who stars as J. Robert Oppenheimer in the film?"
context = """Oppenheimer is a 2023 biographical thriller film written and directed by Christopher Nolan. Based on the 2005 biography American Prometheus by Kai Bird and Martin J. Sherwin, the film chronicles the life of J. Robert Oppenheimer, a theoretical physicist who was pivotal in developing the first nuclear weapons as part of the Manhattan Project, and thereby ushering in the Atomic Age. Cillian Murphy stars as Oppenheimer, with Emily Blunt as Oppenheimer's wife Katherine "Kitty" Oppenheimer."""
good_answer = "Christopher Nolan directed the film Oppenheimer. Cillian Murphy stars as J. Robert Oppenheimer in the film."
bad_answer = "James Cameron directed the film Oppenheimer. Tom Cruise stars as J. Robert Oppenheimer in the film."

evaluator = RAGASEvaluator(api_key=API_KEY, base_url=BASE_URL, llm_model=MODEL, embedding_model=EMBEDDING_MODEL)

print("=== Evaluating Good Answer (Faithful) ===")
result_good = evaluator.evaluate(question, good_answer, context)
print(f"Faithfulness: {result_good.faithfulness:.3f}")
print(f"Answer Relevancy: {result_good.answer_relevancy:.3f}")
print(f"Context Relevancy: {result_good.context_relevancy:.3f}")

print("\n=== Evaluating Bad Answer (Unfaithful) ===")
result_bad = evaluator.evaluate(question, bad_answer, context)
print(f"Faithfulness: {result_bad.faithfulness:.3f}")
print(f"Answer Relevancy: {result_bad.answer_relevancy:.3f}")
print(f"Context Relevancy: {result_bad.context_relevancy:.3f}")