from typing import Dict
from app.models.case import PatientCase

CASE_DB: Dict[str, PatientCase] = {}

def save_case(case: PatientCase):
    CASE_DB[case.case_id] = case

def get_case(case_id: str):
    return CASE_DB.get(case_id)