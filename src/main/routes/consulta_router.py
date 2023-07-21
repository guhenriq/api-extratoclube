from fastapi import APIRouter
from src.main.schemas import schemas

router = APIRouter()

@router.post('/consulta-matricula')
def consultar_matricula(data: schemas.ConsultaMatriculaSchema):
    return data

