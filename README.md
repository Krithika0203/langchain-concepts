# 🧠 LangChain Concepts

> Explore the building blocks of modern AI — text generation, summarization, translation, and prompt templates — all in clean, beginner-friendly Python.

---

## 📁 Project Structure

```
langchain-concepts/
├── utilities.py           # API setup (shared across all files)
├── 1_text_generation.py   # Ask questions, get answers
├── 2_summarization.py     # Condense long text instantly
├── 3_translation.py       # Translate into any language
├── 4_prompt_templates.py  # Reusable, dynamic prompts
├── .env                   # Your API key (keep this private)
└── requirements.txt       # Dependencies
```

---

## 💡 What Each File Does

| File | Concept | What it teaches |
|---|---|---|
| `utilities.py` | Configuration | Load API key once, reuse everywhere |
| `1_text_generation.py` | HumanMessage | Wrap prompts and get LLM responses |
| `2_summarization.py` | HumanMessage | Condense text into paragraphs or bullets |
| `3_translation.py` | HumanMessage | Translate to French, Japanese, Tamil & more |
| `4_prompt_templates.py` | PromptTemplate | Dynamic, reusable prompt structures |

---

## 🔑 Key Concept

All four use cases use the **same** `HumanMessage` class — what changes is the *prompt* inside it.

```python
from langchain_core.messages import HumanMessage

message = HumanMessage(content="Your prompt here")
response = llm.invoke([message])
print(response.content)
```
