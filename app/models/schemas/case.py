from pydantic import BaseModel
from datetime import datetime

# This is the response schema for the case
# It is used to validate the response from the API
# keeps api stable if db changes
# never expose internal db models directly to the api
class CaseResponse(BaseModel):
    id: int
    case_id: str
    patient_age: int
    patient_gender: str
    symptom_text: str
    triage_level: str
    triage_reason: str
    created_at: datetime

    class Config:
        from_attributes = True