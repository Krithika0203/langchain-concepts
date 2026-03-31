"""
utilities.py
------------
Central configuration for Groq API key and model initialization.
Import from this file in all other scripts.
"""

import os
from dotenv import load_dotenv

# Load .env file automatically
load_dotenv()


def get_api_key() -> str:
    """
    Read GROQ_API_KEY from environment.
    Raises a clear error if the key is missing.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GROQ_API_KEY not found!\n"
            "Please open the .env file and set your Groq API key.\n"
            "Get your key at: https://console.groq.com/keys"
        )
    return api_key


def get_llm():
    """
    Initialize and return the Groq LLM (llama-3.3-70b-versatile).
    Used for text generation, summarization, and translation.
    """
    from langchain_groq import ChatGroq

    api_key = get_api_key()

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=api_key,
        temperature=0.7,
    )
    return llm


# Quick test — run: python utilities.py
if __name__ == "__main__":
    print("Testing Groq setup...")
    try:
        key = get_api_key()
        print(f"  API key loaded: {'*' * (len(key) - 4)}{key[-4:]}")
        llm = get_llm()
        print(f"  Model ready   : {llm.model_name}")
        print("\nSetup OK! You can now run the other scripts.")
    except Exception as e:
        print(f"\nERROR: {e}")
