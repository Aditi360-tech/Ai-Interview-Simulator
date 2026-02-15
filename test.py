from interview_engine.evaluator import evaluate_answer
from llm.llm_config import get_llm

llm = get_llm()

question = "Explain what a REST API is."
answer = """
A REST API is an interface that allows communication between client and server using HTTP methods like GET and POST.
"""

feedback = evaluate_answer(llm, question, answer)

print("\n--- Feedback ---")
print("Score:", feedback.score)
print("Strengths:", feedback.strengths)
print("Weaknesses:", feedback.weaknesses)
print("Improvement:", feedback.improvement)