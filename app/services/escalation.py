def requires_doctor_review(
    risk_level: str,
    ai_used: bool,
    consent: bool
) -> bool:
    if not consent:
        return False

    if risk_level == "HIGH":
        return True

    if risk_level == "MEDIUM":
        return True

    if ai_used and risk_level == "LOW":
        return True

    return False