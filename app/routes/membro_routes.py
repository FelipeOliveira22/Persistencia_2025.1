from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.membro import Membro
from app.database import engine

router = APIRouter(prefix="/membros", tags=["Membros"])

@router.post("/", response_model=Membro)
def create_membro(membro: Membro):
    with Session(engine) as session:
        session.add(membro)
        session.commit()
        session.refresh(membro)
        return membro

@router.get("/", response_model=list[Membro])
def read_membros():
    with Session(engine) as session:
        return session.exec(select(Membro)).all()
