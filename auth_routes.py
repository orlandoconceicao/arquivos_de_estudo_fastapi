from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session 

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Rota de autenticação do sistema.
    """
    return {"mensagem": "mensagem"}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):# session vai ser o parametro que o usuario vai mandar
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()# Puxando sessao
    if usuario: 
        # ja existe um usuario com esse email
        raise HTTPException(status_code=400, detail="E-mail de usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        
        # TRANSFORMA O SCHEMA EM DICIONÁRIO (O PULO DO GATO DO LIRA)
        dados_usuario = usuario_schema.model_dump()
        dados_usuario["senha"] = senha_criptografada
        
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)# Suficiente para criar um usuario =>
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem": f"usuário criado com sucesso {usuario_schema.email}"}#  <=