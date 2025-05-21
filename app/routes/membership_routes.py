from fastapi import APIRouter
from sqlmodel import Session, select
from app.models.membership import Membership
from app.database import engine

router = APIRouter(prefix="/memberships", tags=["Memberships"])

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
