import os
from dotenv import load_dotenv
from src.evaluator import RAGASEvaluator

load_dotenv()

API_KEY = os.getenv("GAPGPT_API_KEY")
BASE_URL = os.getenv("GAPGPT_BASE_URL")
MODEL = os.getenv("DEFAULT_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# Table 2: Example from WikiEval, showing answers with high and low answer relevance.
question = "When is the scheduled launch date and time for the PSLV-C56 mission, and where will it be launched from?"
high_answer_relevance = "The PSLV-C56 mission is scheduled to be launched on Sunday, 30 July 2023 at 06:30 IST / 01:00 UTC. It will be launched from the Satish Dhawan Space Centre, Sriharikota, Andhra Pradesh, India."
low_answer_relevance = "The scheduled launch date and time for the PSLV-C56 mission have not been provided. The PSLV-C56 mission is an important space mission for India. It aims to launch a satellite into orbit to study weather patterns."

evaluator = RAGASEvaluator(api_key=API_KEY, base_url=BASE_URL, llm_model=MODEL, embedding_model=EMBEDDING_MODEL)

print("=== Evaluating High Answer Relevance ===")
result_good = evaluator.evaluate(question, high_answer_relevance)
print(f"Answer Relevancy: {result_good.answer_relevancy:.3f}")

print("\n=== Evaluating Low Answer Relevance ===")
result_bad = evaluator.evaluate(question, low_answer_relevance)
print(f"Answer Relevancy: {result_bad.answer_relevancy:.3f}")