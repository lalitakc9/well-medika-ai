from pydantic import BaseModel

class PatientIntakeRequest(BaseModel):
    patient_age: int
    patient_gender: str
    symptom_text: str
    consent: bool

class PatientIntakeResponse(BaseModel):
    case_id: str
    status: str
    message: str