"""
1_text_generation.py
--------------------
Text generation using HumanMessage from LangChain + Groq.

Run:
    python 1_text_generation.py
"""

from langchain_core.messages import HumanMessage
from utilities import get_llm


def generate_text(prompt: str) -> str:
    """Send a prompt to the LLM and return the response."""
    llm = get_llm()
    message = HumanMessage(content=prompt)
    response = llm.invoke([message])
    return response.content


if __name__ == "__main__":
    print("=" * 50)
    print("       TEXT GENERATION WITH GROQ")
    print("=" * 50)

    questions = [
        "What is artificial intelligence?",
        "Explain what an API is in simple terms.",
        "Write a 2-line motivational quote about learning.",
    ]

    for q in questions:
        print(f"\nQuestion : {q}")
        print(f"Answer   : {generate_text(q)}")
        print("-" * 50)

    # ── Interactive mode ──────────────────────────────
    print("\nEntering interactive mode. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit", "q"):
            print("Bye!")
            break
        if user_input:
            print(f"AI : {generate_text(user_input)}\n")
