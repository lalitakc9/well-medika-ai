from app.services.triage_engine import run_triage
from app.services.case_store import save_case
from app.models.case import PatientCase

def process_case(case: PatientCase):
    triage_result = run_triage(case.symptom_text)

    case.risk_level = triage_result["risk_level"]
    case.emergency = triage_result["emergency"]

    if case.emergency:
        case.status = "escalated"
    else:
        case.status = "under_review"

    save_case(case)