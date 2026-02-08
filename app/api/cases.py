from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.db_case import PatientCase
from app.models.schemas.case import CaseResponse

router = APIRouter(prefix="/api/cases", tags=["Cases"])

@router.get("/", response_model=list[CaseResponse])
def list_cases(db: Session = Depends(get_db)):
    cases = (
        db.query(PatientCase)
        .order_by(PatientCase.created_at.desc())
        .all()
    )

# convert db objects to pydantic models
    response = []
    for c in cases:
        response.append({
            "id": c.id,
            "case_id": f"CASE_{c.id:05d}",
            "patient_age": c.patient_age,
            "patient_gender": c.patient_gender,
            "symptom_text": c.symptom_text,
            "triage_level": c.triage_level,
            "triage_reason": c.triage_reason,
            "created_at": c.created_at,
        })

    return response