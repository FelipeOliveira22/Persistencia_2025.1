from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.membership import Membership
from app.database import engine

router = APIRouter(prefix="/memberships", tags=["Membership"])

@router.post("/", response_model=Membership)
def create_membership(membership: Membership):
    with Session(engine) as session:
        session.add(membership)
        session.commit()
        session.refresh(membership)
        return membership

@router.get("/", response_model=list[Membership])
def read_memberships():
    with Session(engine) as session:
        return session.exec(select(Membership)).all()

@router.get("/{id}", response_model=Membership)
def read_membership_by_id(id: int):
    with Session(engine) as session:
        membership = session.get(Membership, id)
        if not membership:
            raise HTTPException(status_code=404, detail="Membership não encontrado")
        return membership

@router.put("/{id}", response_model=Membership)
def update_membership(id: int, dados: Membership):
    with Session(engine) as session:
        membership = session.get(Membership, id)
        if not membership:
            raise HTTPException(status_code=404, detail="Membership não encontrado")
        for key, value in dados.dict().items():
            setattr(membership, key, value)
        session.commit()
        session.refresh(membership)
        return membership

@router.delete("/{id}")
def delete_membership(id: int):
    with Session(engine) as session:
        membership = session.get(Membership, id)
        if not membership:
            raise HTTPException(status_code=404, detail="Membership não encontrado")
        session.delete(membership)
        session.commit()
        return {"ok": True}
