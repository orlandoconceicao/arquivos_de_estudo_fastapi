from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    """
    Rota de pedidos do sistema.
    """
    return {"mensagem: voce acessou a rota de pedidos"}
    