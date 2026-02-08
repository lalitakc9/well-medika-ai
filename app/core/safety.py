EMERGENCY_KEYWORDS = [
    "chest pain",
    "shortness of breath",
    "unconscious",
    "severe bleeding",
    "stroke",
    "heart attack"
]

def is_emergency(symptoms: str) -> bool:
    symptoms = symptoms.lower()
    return any(keyword in symptoms for keyword in EMERGENCY_KEYWORDS)
