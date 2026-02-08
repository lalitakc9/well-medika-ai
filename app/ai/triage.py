RED_FLAGS = ["chest pain", "shortness of breath"]

def triage(symptoms: dict) -> dict:
    if symptoms.get("primary_symptom") in RED_FLAGS:
        return {
            "risk_level": "HIGH",
            "explanation": "Red flag symptom detected"
        }
    return {
        "risk_level": "LOW",
        "explanation": "No high-risk indicators"
    }