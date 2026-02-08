from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from app.db import Base

class TriageRequest(BaseModel):
    patient_age: int = Field(..., ge=0, le=120)
    patient_gender: str
    symptom_text: str
    consent: bool

class TriageResponse(BaseModel):
    risk_level: str
    recommendation: str
    emergency: bool

class TriageResult(Base):
    __tablename__ = "triage_results"

    id = Column(Integer, primary_key=True, index=True)

    symptoms = Column(JSON, nullable=False)
    triage_level = Column(String(20), nullable=False)
    message = Column(String, nullable=False)
    action = Column(String, nullable=False)

    consent_given = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())