def calculate_confidence(risk_level: str, ai_used: bool) -> float:
    if risk_level == "HIGH":
        return 0.95

    if risk_level == "MEDIUM":
        return 0.85 if ai_used else 0.80

    # LOW risk
    return 0.75 if ai_used else 0.65