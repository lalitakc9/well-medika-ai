# app/services/rule_triage.py

HIGH_RISK_KEYWORDS = [
    "chest pain",
    "shortness of breath",
    "loss of consciousness",
    "severe bleeding",
    "stroke",
    "heart attack"
]

MEDIUM_RISK_KEYWORDS = [
    "persistent headache",
    "nausea",
    "dizziness",
    "fever",
    "vomiting",
    "abdominal pain",
    "red urine",
    "blood in urine",
    "hematuria",
    "dark urine",
    "burning urination"
]


def rule_based_triage(symptom_text: str) -> dict:
    text = symptom_text.lower()

    for keyword in HIGH_RISK_KEYWORDS:
        if keyword in text:
            return {
                "risk_level": "HIGH",
                "recommendation": "Seek emergency medical care immediately.",
                "matched_keyword": keyword,
                "rule_source": "rule_based_triage"
            }

    for keyword in MEDIUM_RISK_KEYWORDS:
        if keyword in text:
            return {
                "risk_level": "MEDIUM",
                "recommendation": "Consult a doctor within 24–48 hours.",
                "matched_keyword": keyword,
                "rule_source": "rule_based_triage"
            }

    return {
        "risk_level": "LOW",
        "recommendation": "Symptoms appear mild. Monitor and practice self-care.",
        "matched_keyword": None,
        "rule_source": "rule_based_triage"
    }
