"""
4_prompt_templates.py
---------------------
Reusable prompt templates using LangChain's PromptTemplate + Groq.

Instead of hardcoding strings, templates use named variables
(e.g. {sentence}, {language}) filled at runtime.

Run:
    python 4_prompt_templates.py
"""

from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage
from utilities import get_llm


# ── Template 1: Professional Tone Rephraser ──────────────
REPHRASE_TEMPLATE = PromptTemplate(
    template=(
        "Rephrase the following sentence into a more professional and formal tone. "
        "Return only the rephrased sentence:\n\n"
        "Sentence: {sentence}"
    ),
    input_variables=["sentence"],
)


def rephrase_professionally(sentence: str) -> str:
    llm = get_llm()
    prompt = REPHRASE_TEMPLATE.format(sentence=sentence)
    return llm.invoke([HumanMessage(content=prompt)]).content


# ── Template 2: Translation Template ─────────────────────
TRANSLATION_TEMPLATE = PromptTemplate(
    template=(
        "Translate the following text into {language}. "
        "Return only the translated text:\n\n{text}"
    ),
    input_variables=["language", "text"],
)


def translate_with_template(text: str, language: str) -> str:
    llm = get_llm()
    prompt = TRANSLATION_TEMPLATE.format(text=text, language=language)
    return llm.invoke([HumanMessage(content=prompt)]).content


# ── Template 3: Audience-aware Explainer ─────────────────
EXPLAINER_TEMPLATE = PromptTemplate(
    template=(
        "Explain '{topic}' in simple terms that a {audience} would understand. "
        "Use an analogy if helpful. Keep it under 80 words."
    ),
    input_variables=["topic", "audience"],
)


def explain_topic(topic: str, audience: str) -> str:
    llm = get_llm()
    prompt = EXPLAINER_TEMPLATE.format(topic=topic, audience=audience)
    return llm.invoke([HumanMessage(content=prompt)]).content


# ── Template 4: Domain Expert Q&A (ChatPromptTemplate) ───
CHAT_TEMPLATE = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful expert in {domain}."),
    ("human", "{question}"),
])


def ask_domain_expert(domain: str, question: str) -> str:
    llm = get_llm()
    messages = CHAT_TEMPLATE.format_messages(domain=domain, question=question)
    return llm.invoke(messages).content


if __name__ == "__main__":
    print("=" * 50)
    print("       PROMPT TEMPLATES WITH GROQ")
    print("=" * 50)

    # 1. Tone rephrasing
    casual = "hey can you fix this? it's been broken forever and it's really annoying"
    print(f"\n[Rephrase] Original : {casual}")
    print(f"[Rephrase] Formal   : {rephrase_professionally(casual)}")

    # 2. Translation template
    text = "Learning never stops, and every day is a new opportunity."
    print(f"\n[Translate] English : {text}")
    print(f"[Translate] French  : {translate_with_template(text, 'French')}")
    print(f"[Translate] Tamil   : {translate_with_template(text, 'Tamil')}")

    # 3. Audience-aware explainer
    print(f"\n[Explain] Machine Learning for a 10-year-old:")
    print(explain_topic("machine learning", "10-year-old"))
    print(f"\n[Explain] Machine Learning for a software engineer:")
    print(explain_topic("machine learning", "software engineer"))

    # 4. Domain expert Q&A
    print(f"\n[Expert] Finance Q&A:")
    print(ask_domain_expert("personal finance", "What is compound interest?"))

    # ── Interactive mode ──────────────────────────────────
    print("\n" + "=" * 50)
    print("Interactive mode")
    print("1. Rephrase  2. Translate  3. Explain  4. Expert Q&A")
    print("Type 'exit' to quit.\n")

    while True:
        choice = input("Choose (1/2/3/4) or 'exit': ").strip()

        if choice.lower() in ("exit", "quit"):
            print("Bye!")
            break

        elif choice == "1":
            s = input("Enter sentence: ").strip()
            print(f"Rephrased: {rephrase_professionally(s)}\n")

        elif choice == "2":
            t = input("Text: ").strip()
            l = input("Language: ").strip()
            print(f"Translated: {translate_with_template(t, l)}\n")

        elif choice == "3":
            topic = input("Topic: ").strip()
            audience = input("Audience: ").strip()
            print(f"Explanation: {explain_topic(topic, audience)}\n")

        elif choice == "4":
            domain = input("Domain (e.g. finance, medicine): ").strip()
            question = input("Your question: ").strip()
            print(f"Answer: {ask_domain_expert(domain, question)}\n")

        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.\n")
