from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routes import (
    equipe_routes,
    membro_routes,
    projeto_routes,
    tarefa_routes,
    membership_routes
)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(equipe_routes.router)
app.include_router(membro_routes.router)
app.include_router(projeto_routes.router)
app.include_router(tarefa_routes.router)
app.include_router(membership_routes.router)

@app.get("/")
def read_root():
    return {"msg": "API ativa"}
