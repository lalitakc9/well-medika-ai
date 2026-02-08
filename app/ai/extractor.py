def extract_symptoms(text: str) -> dict:
    return {
        "primary_symptom": "chest pain" if "chest" in text.lower() else "unknown"
    }