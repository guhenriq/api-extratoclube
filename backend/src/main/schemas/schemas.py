from pydantic import BaseModel

class ConsultaMatriculaSchema(BaseModel):
    cpfCliente: str
    loginPortal: str
    senhaPortal: str
