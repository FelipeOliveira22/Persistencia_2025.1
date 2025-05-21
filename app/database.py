from sqlmodel import SQLModel, create_engine
from app.models.equipe import Equipe
from app.models.membro import Membro
from app.models.projeto import Projeto
from app.models.tarefa import Tarefa
from app.models.membership import Membership

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
