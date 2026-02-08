def explain(flags: dict, age: int):
    reasons = []

    if flags.get("blood_in_urine"):
        reasons.append("Possible blood in urine detected")
    if age >= 40:
        reasons.append("Age increases risk factors")

    return reasons
