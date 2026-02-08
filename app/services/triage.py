def run_triage(symptoms: list[str]) -> dict:
    emergency_symptoms = {"chest pain", "shortness of breath", "unconsciousness"}

    if any(s in emergency_symptoms for s in symptoms):
        return {
            "level": "emergency",
            "message": "Potential medical emergency detected.",
            "action": "Seek immediate medical attention."
        }

    if len(symptoms) >= 3:
        return {
            "level": "medium",
            "message": "Multiple symptoms reported.",
            "action": "Consider consulting a doctor."
        }

    return {
        "level": "low",
        "message": "Symptoms appear mild.",
        "action": "Monitor symptoms and rest."
    }