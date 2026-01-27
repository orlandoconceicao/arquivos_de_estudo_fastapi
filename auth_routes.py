from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Rota de autenticação do sistema.
    """
    return {"mensagem": "mensagem"}