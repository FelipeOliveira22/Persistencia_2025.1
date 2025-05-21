from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.projeto import Projeto

class Tarefa(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    descricao: str
    projeto_id: int = Field(foreign_key="projeto.id")

    projeto: Optional["Projeto"] = Relationship(back_populates="tarefas")
