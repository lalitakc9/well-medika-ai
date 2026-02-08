def get_age_risk(age: int) -> int:
    if age >= 60:
        return 2
    if age >= 40:
        return 1
    return 0
