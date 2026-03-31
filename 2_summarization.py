"""
2_summarization.py
------------------
Text summarization using HumanMessage from LangChain + Groq.

Run:
    python 2_summarization.py
"""

from langchain_core.messages import HumanMessage
from utilities import get_llm


def summarize_text(text: str, style: str = "paragraph") -> str:
    """
    Summarize the given text.

    Args:
        text  : The text to summarize.
        style : 'paragraph' (default) or 'bullets'
    """
    llm = get_llm()

    if style == "bullets":
        instruction = (
            "Summarize the following text as concise bullet points. "
            "Each bullet should capture one key idea:\n\n"
        )
    else:
        instruction = (
            "Summarize the following text in 2-3 clear sentences. "
            "Keep the main ideas:\n\n"
        )

    message = HumanMessage(content=instruction + text)
    response = llm.invoke([message])
    return response.content


SAMPLE_TEXT = """
Artificial intelligence (AI) is intelligence demonstrated by machines,
as opposed to the natural intelligence displayed by humans and animals.
AI research has been defined as the field of study of intelligent agents,
which refers to any system that perceives its environment and takes actions
that maximize its chance of achieving its goals.

AI applications include advanced web search engines, recommendation systems,
understanding human speech, self-driving cars, generative AI, and competing
at the highest level in strategic game systems. As machines become increasingly
capable, tasks considered to require intelligence are often removed from the
definition of AI, a phenomenon known as the AI effect.
"""

if __name__ == "__main__":
    print("=" * 50)
    print("         SUMMARIZATION WITH GROQ")
    print("=" * 50)

    print("\nOriginal text:")
    print(SAMPLE_TEXT.strip())

    print("\n--- Paragraph Summary ---")
    print(summarize_text(SAMPLE_TEXT, style="paragraph"))

    print("\n--- Bullet Point Summary ---")
    print(summarize_text(SAMPLE_TEXT, style="bullets"))

    # ── Interactive mode ──────────────────────────────
    print("\n" + "=" * 50)
    print("Interactive mode: paste your text, press Enter twice.")
    print("Type 'exit' to quit.\n")

    while True:
        print("Enter text:")
        lines = []
        while True:
            line = input()
            if line.lower() in ("exit", "quit"):
                print("Bye!")
                exit()
            if line == "":
                break
            lines.append(line)

        text = "\n".join(lines).strip()
        if not text:
            continue

        style = input("Style? (paragraph / bullets) [paragraph]: ").strip() or "paragraph"
        print(f"\nSummary:\n{summarize_text(text, style=style)}\n")
        print("-" * 50)
