from app.services.triage.risk_engine import calculate_risk


def test_blood_urine_medium_risk():
    level, score, flags = calculate_risk(50, "red urine")  # pyright: ignore[reportUnusedVariable]
    assert level == "MEDIUM"