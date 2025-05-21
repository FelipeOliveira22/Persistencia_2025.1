from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.tarefa import Tarefa
    from app.models.equipe import Equipe

class Projeto(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    descricao: Optional[str] = None
    equipe_id: int = Field(foreign_key="equipe.id")

    equipe: Optional["Equipe"] = Relationship(back_populates="projetos")
    tarefas: List["Tarefa"] = Relationship(back_populates="projeto")
