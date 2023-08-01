from fastapi import APIRouter
from fastapi.responses import JSONResponse
from celery import chain
from src.main.schemas import schemas
from src.externals.message import tasks

router = APIRouter()

@router.post('/solicitacao-matricula')
def solicitacao_matricula(data: schemas.ConsultaMatriculaSchema):

    workflow = chain(
        tasks.verify_cached_data.s(data.cpfCliente),
        tasks.extract_data.s(username=data.loginPortal, password=data.senhaPortal),
        tasks.save_in_cache.s(),
        tasks.index_data.s()
    ).apply_async()

    data = {
        'message': 'solicitação recebida', 
        'id_solicitacao': workflow.id
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
