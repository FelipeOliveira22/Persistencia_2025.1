from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.equipe import Equipe
from app.database import engine

router = APIRouter(prefix="/equipes", tags=["Equipes"])

@router.post("/", response_model=Equipe)
def create_equipe(equipe: Equipe):
    with Session(engine) as session:
        session.add(equipe)
        session.commit()
        session.refresh(equipe)
        return equipe

@router.get("/", response_model=list[Equipe])
def read_equipes():
    with Session(engine) as session:
        return session.exec(select(Equipe)).all()

@router.get("/{equipe_id}", response_model=Equipe)
def read_equipe(equipe_id: int):
    with Session(engine) as session:
        equipe = session.get(Equipe, equipe_id)
        if not equipe:
            raise HTTPException(status_code=404, detail="Equipe não encontrada")
        return equipe

@router.delete("/{equipe_id}")
def delete_equipe(equipe_id: int):
    with Session(engine) as session:
        equipe = session.get(Equipe, equipe_id)
        if not equipe:
            raise HTTPException(status_code=404, detail="Equipe não encontrada")
        session.delete(equipe)
        session.commit()
        return {"ok": True}
