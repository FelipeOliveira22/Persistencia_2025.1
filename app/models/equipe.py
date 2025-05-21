from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.membro import Membro
    from app.models.projeto import Projeto

class Equipe(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    descricao: Optional[str] = None

    membros: List["Membro"] = Relationship(back_populates="equipe")
    projetos: List["Projeto"] = Relationship(back_populates="equipe")
