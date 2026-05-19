import os
from dotenv import load_dotenv
from src.evaluator import RAGASEvaluator

load_dotenv()

API_KEY = os.getenv("GAPGPT_API_KEY")
BASE_URL = os.getenv("GAPGPT_BASE_URL")
MODEL = os.getenv("DEFAULT_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# Table 3: Example from WikiEval, showing answers with high and low context relevance.
question = "When was the Chimnabai Clock Tower completed, and who was it named after?"
high_context_relevance = "The Chimnabai Clock Tower, also known as the Raopura Tower, is a clock tower situated in the Raopura area of Vadodara, Gujarat, India. It was completed in 1896 and named in memory of Chimnabai I (1864-1885), a queen and the first wife of Sayajirao Gaekwad III of Baroda State."
Low_context_relevance = "The Chimnabai Clock Tower, also known as the Raopura Tower, is a clock tower situated in the Raopura area of Vadodara, Gujarat, India. It was completed in 1896 and named in memory of Chimnabai I (1864-1885), a queen and the first wife of Sayajirao Gaekwad III of Baroda State. It was built in Indo-Saracenic architecture style. History. Chimnabai Clock Tower was built in 1896. The tower was named after Chimnabai I (1864-1885), a queen and the first wife of Sayajirao Gaekwad III of Baroda State. It was inaugurated by Mir Kamaluddin Hussainkhan, the last Nawab of Baroda. During the rule of Gaekwad, it was a stoppage for horse drawn trams. The clock tower was erected at the cost of 25,000 (equivalent to 9.2 million or USD 120,000 in 2023)."
answer = "The Chimnabai Clock Tower was completed in 1896 and named after Chimnabai I."

evaluator = RAGASEvaluator(api_key=API_KEY, base_url=BASE_URL, llm_model=MODEL, embedding_model=EMBEDDING_MODEL)

print("=== Evaluating High Context Relevance ===")
result_good = evaluator.evaluate(question=question, answer=answer, context=high_context_relevance)
print(f"Context Relevancy: {result_good.context_relevancy:.3f}")

print("\n=== Evaluating Low Context Relevance ===")
result_bad = evaluator.evaluate(question=question, answer=answer, context=Low_context_relevance)
print(f"Context Relevancy: {result_bad.context_relevancy:.3f}")