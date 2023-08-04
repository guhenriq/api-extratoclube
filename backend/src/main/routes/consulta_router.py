from fastapi import APIRouter
from fastapi.responses import JSONResponse
from celery import chain
from src.main.schemas import schemas
from src.externals.message import tasks
from src.externals.elasticsearch import ElasticConnection

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

@router.get('/consultar-matricula/{cpf}')
def consultar_solicitacao_matricula(cpf: str):
    es = ElasticConnection()
    es_conn = es.get_connection()
    
    try:
        resultado = es_conn.get(index='matriculas', id=cpf)
        response = resultado['_source']
        
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        return JSONResponse(content={'msg': 'dados para cpf não encontrado'})
    
@router.get('/status-solicitacao/{task_id}')
def status_solicitacao(task_id: str):
    result = tasks.app.AsyncResult(task_id, app=tasks.app)

    try:
        if result.successful():
            status = 'tarefa concluida'
        elif result.failed():
            status = 'tarefa falhou'
        elif result.status == 'PENDING':
            status = 'tarefa pendente'
        elif result.status == 'STARTED':
            status = 'tarefa em andamento'
        elif result.status == 'REVOKED':
            status = 'tarefa cancelada ou revogada'
        elif result.status == 'RETRY':
            status = 'tarefa falhou mas será reexecutada'
        elif result.status == 'RECEIVED':
            status = 'tarefa recebida mas não atribuida ao worker'
        else:
            status = 'tarefa desconhecida'
        
        response = {'status': status}

        return JSONResponse(content=response, status_code=200)
    except:
        response = {'status': 'erro ao tentar consultar tarefa'}
        return JSONResponse(content=response, status_code=404)
    
