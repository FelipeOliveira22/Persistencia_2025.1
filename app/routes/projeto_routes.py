from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.projeto import Projeto
from app.database import engine

router = APIRouter(prefix="/projetos", tags=["Projetos"])

@router.post("/", response_model=Projeto)
def create_projeto(projeto: Projeto):
    with Session(engine) as session:
        session.add(projeto)
        session.commit()
        session.refresh(projeto)
        return projeto

@router.get("/", response_model=list[Projeto])
def read_projetos():
    with Session(engine) as session:
        return session.exec(select(Projeto)).all()
