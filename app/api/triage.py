# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from app.db import get_db
# from app.models.db_case import PatientCase
# from app.services.triage_engine import run_triage
# from app.schemas.triage import TriageRequest

# router = APIRouter()

# @router.post("/triage")
# def triage_patient(
#     request: TriageRequest,
#     db: Session = Depends(get_db)
# ):
#     # Run triage logic
#     triage_result = run_triage(request.symptom_text)

#     # ✅ CREATE DB OBJECT
#     case = PatientCase(
#         patient_age=request.patient_age,
#         patient_gender=request.patient_gender,
#         symptom_text=request.symptom_text,
#         ai_summary=triage_result["ai_summary"],
#         emergency=triage_result["emergency"]
#     )

#     # ✅ SAVE TO DATABASE
#     db.add(case)
#     db.commit()
#     db.refresh(case)

#     return {
#         "case_id": case.id,
#         "risk_level": triage_result["risk_level"],
#         "emergency": triage_result["emergency"],
#         "ai_summary": triage_result["ai_summary"]
#     }

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.db_case import PatientCase
from app.schemas.triage import TriageRequest  # pyright: ignore[reportMissingImports]
from app.services.triage.risk_engine import calculate_risk
from app.services.triage.decision_explainer import explain
from app.services.triage_engine import run_triage  # AI summary only

router = APIRouter()

@router.post("/triage")
def triage_patient(
    request: TriageRequest,
    db: Session = Depends(get_db)
):
    # 1️⃣ Deterministic clinical reasoning
    risk_level, score, flags = calculate_risk(
        age=request.patient_age,
        symptom_text=request.symptom_text
    )

    # 2️⃣ Explainable reasoning
    reasons = explain(flags, request.patient_age)

    # 3️⃣ AI summary (NOT decision-making)
    ai_summary = run_triage(request.symptom_text)["recommendation"]

    emergency = risk_level == "HIGH"

    # 4️⃣ Persist case
    case = PatientCase(
        patient_age=request.patient_age,
        patient_gender=request.patient_gender,
        symptom_text=request.symptom_text,
        risk_level=risk_level,
        risk_score=score,
        emergency=emergency,
        reasoning="; ".join(reasons),
        ai_summary=ai_summary,
        consent=request.consent
    )

    db.add(case)
    db.commit()
    db.refresh(case)

    return {
        "case_id": f"CASE_{case.id:05d}",
        "risk_level": risk_level,
        "risk_score": score,
        "emergency": emergency,
        "reasons": reasons,
        "ai_summary": ai_summary
    }
