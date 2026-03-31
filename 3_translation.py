"""
3_translation.py
----------------
Text translation using HumanMessage from LangChain + Groq.

Run:
    python 3_translation.py
"""

from langchain_core.messages import HumanMessage
from utilities import get_llm


def translate_text(text: str, target_language: str) -> str:
    """
    Translate text into the target language.

    Args:
        text            : Source text (any language).
        target_language : E.g. 'French', 'Japanese', 'Tamil', 'Spanish'.
    """
    llm = get_llm()

    prompt = (
        f"Translate the following text into {target_language}. "
        f"Preserve the original meaning and named entities. "
        f"Return only the translated text:\n\n{text}"
    )

    message = HumanMessage(content=prompt)
    response = llm.invoke([message])
    return response.content


if __name__ == "__main__":
    print("=" * 50)
    print("          TRANSLATION WITH GROQ")
    print("=" * 50)

    sample = "Hello! I am learning about artificial intelligence and large language models."

    languages = ["French", "Spanish", "Japanese", "Tamil"]

    print(f"\nSource (English): {sample}\n")
    for lang in languages:
        print(f"[{lang}]: {translate_text(sample, lang)}")

    # ── Interactive mode ──────────────────────────────
    print("\n" + "=" * 50)
    print("Interactive mode. Type 'exit' to quit.\n")

    while True:
        text = input("Text to translate: ").strip()
        if text.lower() in ("exit", "quit", "q"):
            print("Bye!")
            break
        if not text:
            continue

        lang = input("Translate to: ").strip()
        if not lang:
            continue

        print(f"\n[{lang}]: {translate_text(text, lang)}\n")
        print("-" * 50)
