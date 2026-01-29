from pydantic import BaseModel
from typing import Optional # isso faz que tenha parametros opcionais 

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]
    
    # isso faz que a class de cima seja vista como um dicionário padrão de py
    class Config:
        from_attributes = True