import os
from dotenv import load_dotenv
from src.evaluator import RAGASEvaluator

load_dotenv()

API_KEY = os.getenv("GAPGPT_API_KEY")
BASE_URL = os.getenv("GAPGPT_BASE_URL")
MODEL = os.getenv("DEFAULT_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# Table1:  Example from WikiEval, showing answers with high and low faithfulness.
question = "Who directed the film Oppenheimer and who stars as J. Robert Oppenheimer in the film?"
context = """Oppenheimer is a 2023 biographical thriller film written and directed by Christopher Nolan. Based on the 2005 biography American Prometheus by Kai Bird and Mar tin J. Sherwin, the film chronicles the life of J. Robert Oppenheimer, a theoretical physicist who was pivotal in developing the first nuclear weapons as part of the Manhattan Project, and thereby ushering in the Atomic Age. Cillian Murphy stars as Oppenheimer, with Emily Blunt as Oppenheimer's wife Katherine "Kitty" Oppenheimer."""
high_faithfulness = "Christopher Nolan directed the film Oppenheimer. Cillian Murphy stars as J. Robert Oppenheimer in the film."
low_faithfulness = "James Cameron directed the film Oppenheimer. Tom Cruise stars as J. Robert Oppenheimer in the film."

evaluator = RAGASEvaluator(api_key=API_KEY, base_url=BASE_URL, llm_model=MODEL, embedding_model=EMBEDDING_MODEL)

print("=== Evaluating High Faithfulness ===")
result_good = evaluator.evaluate(question, high_faithfulness, context)
print(f"Faithfulness: {result_good.faithfulness:.3f}")

print("\n=== Evaluating Low Faithfulness ===")
result_bad = evaluator.evaluate(question, low_faithfulness, context)
print(f"Faithfulness: {result_bad.faithfulness:.3f}")