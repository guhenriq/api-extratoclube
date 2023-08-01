import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.main.schemas import schemas
from src.externals.message import tasks

router = APIRouter()

@router.post('/solicitacao-matricula')
def solicitacao_matricula(data: schemas.ConsultaMatriculaSchema):

    result = tasks.get_benefit.delay(data.cpfCliente, data.loginPortal, data.senhaPortal)

    data = {
        'message': 'solicitação recebida', 
        'id_solicitacao': result.id
    }

    return JSONResponse(content=data, status_code=201)

@router.get('/consultar-matricula/{task_id}')
def consultar_solicitacao_matricula(task_id: str):
    task = tasks.app.AsyncResult(task_id, app=tasks.app)

    if task.ready():
        result = task.get()

        return JSONResponse(content=result, status_code=200)
    else:
        return {'status': 'em andamento'}
