"""
Sample pairwise answer evaluation (pairwise comparison) similar to the paper for measuring agreement with humans
"""
import os
from dotenv import load_dotenv
from src.evaluator import RAGASEvaluator

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv("GAPGPT_API_KEY")
BASE_URL = os.getenv("GAPGPT_BASE_URL", "https://api.gapgpt.app/v1")
MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

# Sample data from the paper (Table 2)
question = "When is the scheduled launch date and time for the PSLV-C56 mission, and where will it be launched from?"
context = "The PSLV-C56 mission is scheduled to be launched on Sunday, 30 July 2023 at 06:30 IST / 01:00 UTC from the Satish Dhawan Space Centre, Sriharikota."
good_answer = "The PSLV-C56 mission is scheduled to be launched on Sunday, 30 July 2023 at 06:30 IST / 01:00 UTC. It will be launched from the Satish Dhawan Space Centre, Sriharikota, Andhra Pradesh, India."
bad_answer = "The scheduled launch date and time for the PSLV-C56 mission have not been provided. The PSLV-C56 mission is an important space mission for India. It aims to launch a satellite into orbit to study weather patterns."

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