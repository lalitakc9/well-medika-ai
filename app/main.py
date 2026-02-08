from fastapi import FastAPI
from app.api.patient import router as patient_router
from app.api import patient, cases

app = FastAPI(title="WellMedica AI")

app.include_router(patient_router)

app.include_router(cases.router)

@app.get("/")
def root():
    return {"status": "WellMedica AI running"}