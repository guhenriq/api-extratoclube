from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.main.routes import consulta_router

app = FastAPI(
    title="API Portal Extrato Clube",
    summary="Consulta de dados de clientes",
    version="1.0.0",
    contact={
        "name": "Gustavo Henrique Oliveira dos Santos",
        "url": "https://www.linkedin.com/in/gustavo-henrique-oliveira-dos-santos-028aa4181/",
        "email": "gustavo.henrique.oliveira50@gmail.com"
    },
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def test():
    return {'status': 'ok'}

app.include_router(consulta_router.router, prefix='/v1', tags=['Consulta de Dados'])