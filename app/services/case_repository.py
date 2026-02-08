from sqlalchemy.ext.asyncio import AsyncSession
from app.models.db_case import PatientCase

async def save_case(db: AsyncSession, case: PatientCase):
    db.add(case)
    await db.commit()

async def get_case(db: AsyncSession, case_id: str):
    return await db.get(PatientCase, case_id)