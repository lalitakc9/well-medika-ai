from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db import Base

class PatientCase(Base):
    __tablename__ = "patient_cases"

    id = Column(Integer, primary_key=True, index=True)
    patient_age = Column(Integer, nullable=False)
    patient_gender = Column(String, nullable=False)
    symptom_text = Column(String, nullable=False)

    triage_level = Column(String, nullable=False)
    triage_reason = Column(String, nullable=False)

    consent = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    requires_review = Column(Boolean, default=False)