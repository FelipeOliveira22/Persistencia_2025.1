from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.equipe import Equipe

class Membro(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    equipe_id: int = Field(foreign_key="equipe.id")

    equipe: Optional["Equipe"] = Relationship(back_populates="membros")
