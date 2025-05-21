from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.membro import Membro
from app.database import engine

router = APIRouter(prefix="/membros", tags=["Membro"])

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

@router.get("/{id}", response_model=Membro)
def read_membro_by_id(id: int):
    with Session(engine) as session:
        membro = session.get(Membro, id)
        if not membro:
            raise HTTPException(status_code=404, detail="Membro não encontrado")
        return membro

@router.put("/{id}", response_model=Membro)
def update_membro(id: int, dados: Membro):
    with Session(engine) as session:
        membro = session.get(Membro, id)
        if not membro:
            raise HTTPException(status_code=404, detail="Membro não encontrado")
        for key, value in dados.dict().items():
            setattr(membro, key, value)
        session.commit()
        session.refresh(membro)
        return membro

@router.delete("/{id}")
def delete_membro(id: int):
    with Session(engine) as session:
        membro = session.get(Membro, id)
        if not membro:
            raise HTTPException(status_code=404, detail="Membro não encontrado")
        session.delete(membro)
        session.commit()
        return {"ok": True}
