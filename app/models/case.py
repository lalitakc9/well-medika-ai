from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class PatientCase(BaseModel):
    # We use Field to set a default unique ID if one isn't provided
    case_id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    patient_age: int
    patient_gender: str
    symptom_text: str
    triage_level: Optional[str] = "PENDING"  # Changed from risk_level
    triage_reason: Optional[str] = None      # Added to store AI explanation
    status: str = "submitted"
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True # Allows Pydantic to read SQLAlchemy objects