from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.tarefa import Tarefa
from app.database import engine

router = APIRouter(prefix="/tarefas", tags=["Tarefa"])

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

@router.get("/{id}", response_model=Tarefa)
def read_tarefa_by_id(id: int):
    with Session(engine) as session:
        tarefa = session.get(Tarefa, id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        return tarefa

@router.put("/{id}", response_model=Tarefa)
def update_tarefa(id: int, dados: Tarefa):
    with Session(engine) as session:
        tarefa = session.get(Tarefa, id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        for key, value in dados.dict().items():
            setattr(tarefa, key, value)
        session.commit()
        session.refresh(tarefa)
        return tarefa

@router.delete("/{id}")
def delete_tarefa(id: int):
    with Session(engine) as session:
        tarefa = session.get(Tarefa, id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        session.delete(tarefa)
        session.commit()
        return {"ok": True}
