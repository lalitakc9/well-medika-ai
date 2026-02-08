# app/services/triage_engine.py

import google.generativeai as genai
import os
import json
from app.services.rule_triage import rule_based_triage

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def run_triage(symptom_text: str) -> dict:
    # 1️⃣ Always run rule-based triage first
    rule_result = rule_based_triage(symptom_text)

    # 2️⃣ HIGH risk → STOP (rules are authoritative)
    if rule_result["risk_level"] == "HIGH":
        return {
            **rule_result,
            "ai_used": False
        }

    # 3️⃣ LOW / MEDIUM → AI can assist
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
        You are a medical triage assistant.
        Analyze the following symptoms:

        {symptom_text}

        Respond ONLY in valid JSON:
        {{
          "risk_level": "LOW or MEDIUM",
          "recommendation": "brief advice"
        }}
        """

        response = model.generate_content(prompt)
        parsed = json.loads(response.text.strip())

        return {
            "risk_level": parsed.get("risk_level", rule_result["risk_level"]),
            "recommendation": parsed.get(
                "recommendation",
                rule_result["recommendation"]
            ) + " This is not a medical diagnosis.",
            "matched_keyword": rule_result.get("matched_keyword"),
            "rule_source": rule_result.get("rule_source"),
            "ai_used": True
        }

    except Exception:
        # 4️⃣ AI failed → fall back safely to rules
        return {
            **rule_result,
            "ai_used": False
        }
