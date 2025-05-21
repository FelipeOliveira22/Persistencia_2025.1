from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.equipe import Equipe
from app.database import engine

router = APIRouter(prefix="/equipes", tags=["Equipe"])

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

@router.get("/{id}", response_model=Equipe)
def read_equipe_by_id(id: int):
    with Session(engine) as session:
        equipe = session.get(Equipe, id)
        if not equipe:
            raise HTTPException(status_code=404, detail="Equipe não encontrada")
        return equipe

@router.put("/{id}", response_model=Equipe)
def update_equipe(id: int, dados: Equipe):
    with Session(engine) as session:
        equipe = session.get(Equipe, id)
        if not equipe:
            raise HTTPException(status_code=404, detail="Equipe não encontrada")
        for key, value in dados.dict().items():
            setattr(equipe, key, value)
        session.commit()
        session.refresh(equipe)
        return equipe

@router.delete("/{id}")
def delete_equipe(id: int):
    with Session(engine) as session:
        equipe = session.get(Equipe, id)
        if not equipe:
            raise HTTPException(status_code=404, detail="Equipe não encontrada")
        session.delete(equipe)
        session.commit()
        return {"ok": True}
