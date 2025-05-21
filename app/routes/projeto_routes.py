from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.projeto import Projeto
from app.database import engine

router = APIRouter(prefix="/projetos", tags=["Projeto"])

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

@router.get("/{id}", response_model=Projeto)
def read_projeto_by_id(id: int):
    with Session(engine) as session:
        projeto = session.get(Projeto, id)
        if not projeto:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")
        return projeto

@router.put("/{id}", response_model=Projeto)
def update_projeto(id: int, dados: Projeto):
    with Session(engine) as session:
        projeto = session.get(Projeto, id)
        if not projeto:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")
        for key, value in dados.dict().items():
            setattr(projeto, key, value)
        session.commit()
        session.refresh(projeto)
        return projeto

@router.delete("/{id}")
def delete_projeto(id: int):
    with Session(engine) as session:
        projeto = session.get(Projeto, id)
        if not projeto:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")
        session.delete(projeto)
        session.commit()
        return {"ok": True}
