from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.tarefa import Tarefa
from app.database import engine

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])

@router.post("/", response_model=Tarefa)
def create_tarefa(tarefa: Tarefa):
    with Session(engine) as session:
        session.add(tarefa)
        session.commit()
        session.refresh(tarefa)
        return tarefa

@router.get("/", response_model=list[Tarefa])
def read_tarefas():
    with Session(engine) as session:
        return session.exec(select(Tarefa)).all()
