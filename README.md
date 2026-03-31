# LangChain with Groq — Core Concepts

Text generation, summarization, translation, and prompt templates using **LangChain + Groq (LLaMA 3.3 70B)**.

---

## Setup & Run (Windows)

### Step 1 — Get your Groq API key
Go to: https://console.groq.com/keys  
Sign up (free) → Create API Key → Copy it

### Step 2 — Install dependencies
Open Command Prompt inside the project folder and run:
```
pip install -r requirements.txt
```

### Step 3 — Add your API key
Open the `.env` file and replace the placeholder:
```
GROQ_API_KEY=your_actual_key_here
```

### Step 4 — Test setup
```
python utilities.py
```
You should see: `Setup OK!`

### Step 5 — Run any script
```
python 1_text_generation.py
python 2_summarization.py
python 3_translation.py
python 4_prompt_templates.py
```

---

## Files

| File | What it does |
|---|---|
| `utilities.py` | Loads API key, creates the Groq LLM — shared by all scripts |
| `1_text_generation.py` | Ask any question and get a response |
| `2_summarization.py` | Paste text → get paragraph or bullet-point summary |
| `3_translation.py` | Translate text into any language |
| `4_prompt_templates.py` | Reusable templates: rephrase, translate, explain, expert Q&A |
| `.env` | Your API key (never share this file) |
| `requirements.txt` | Python packages needed |

---

## Common Errors

| Error | Fix |
|---|---|
| `GROQ_API_KEY not found` | Open `.env` and paste your real key |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `AuthenticationError` | Your API key is wrong — copy it again from console.groq.com |
