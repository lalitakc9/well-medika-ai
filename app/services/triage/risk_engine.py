from .symptom_analyzer import analyze
from .age_risk import get_age_risk

def calculate_risk(age: int, symptom_text: str):
    flags = analyze(symptom_text)
    score = get_age_risk(age)

    if flags["blood_in_urine"]:
        score += 3
    if flags["pain"]:
        score += 2

    if score >= 5:
        return "HIGH", score, flags
    elif score >= 3:
        return "MEDIUM", score, flags
    return "LOW", score, flags
