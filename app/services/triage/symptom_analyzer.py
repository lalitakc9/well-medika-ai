def analyze(symptom_text: str) -> dict:
    return {
        "blood_in_urine": "red urine" in symptom_text.lower(),
        "pain": "pain" in symptom_text.lower(),
        "fever": "fever" in symptom_text.lower(),
    }