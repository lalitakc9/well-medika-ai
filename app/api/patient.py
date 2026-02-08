from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.schemas.triage import TriageRequest
from app.services.confidence import calculate_confidence
from app.services.escalation import requires_doctor_review
from app.services.triage_engine import run_triage
from app.models.db_case import PatientCase
from app.db import get_db

router = APIRouter(prefix="/api/patient", tags=["Patient"])

@router.post("/intake")
def patient_intake(data: TriageRequest, db: Session = Depends(get_db)):
    triage = run_triage(data.symptom_text)

    confidence = calculate_confidence(triage["risk_level"], triage["ai_used"])

    # Determine if this case should be escalated to a doctor
    escalate = requires_doctor_review(triage["risk_level"], triage["ai_used"], data.consent)

    # ✅ Persist ONLY if consent is true
    if data.consent:
        case = PatientCase(
            patient_age=data.patient_age,
            patient_gender=data.patient_gender,
            symptom_text=data.symptom_text,
            triage_level=triage["risk_level"],
            triage_reason=triage["recommendation"],
            consent=data.consent,
            requires_review=escalate,
        )
        db.add(case)
        db.commit()
        db.refresh(case)

        case_id = f"CASE_{case.id:05d}"
    else:
        case_id = "NOT_STORED_NO_CONSENT"

    return {
        "case_id": case_id,
        "status": "submitted",
        "triage_level": triage["risk_level"],
        "confidence": confidence,
        "message": triage["recommendation"],
        # "matched_keyword": triage["matched_keyword"],
        #"rule_source": triage["rule_source"],
        "matched_keyword": triage.get("matched_keyword"),
        "rule_source": triage.get("rule_source"),
        "ai_used": triage["ai_used"],
        "requires_doctor_review": escalate
    }