from pydantic import BaseModel, Field


class TriageRequest(BaseModel):
    patient_age: int = Field(..., ge=0, le=120)
    patient_gender: str
    symptom_text: str
    consent: bool