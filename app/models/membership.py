from sqlmodel import SQLModel, Field

class Membership(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    membro_id: int = Field(foreign_key="membro.id")
    equipe_id: int = Field(foreign_key="equipe.id")
