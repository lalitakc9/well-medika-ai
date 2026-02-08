import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """
You are a healthcare triage assistant.
You do NOT diagnose.
You do NOT prescribe.
You only summarize symptoms and estimate severity.
If symptoms suggest emergency, clearly state so.
"""

def ai_analyze_symptoms(symptom_text: str) -> str:
    prompt = f"""
    {SYSTEM_PROMPT}

    Patient symptoms:
    {symptom_text}

    Provide:
    - Symptom summary
    - Severity level: Low / Medium / High
    """

    response = model.generate_content(prompt)
    return response.text