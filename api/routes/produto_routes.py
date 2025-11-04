from typing import Optional, List
from fastapi import APIRouter
from modules.produto import schemas
from modules.produto.service import ProdutoService

router = APIRouter(prefix="/produto", tags=["Produto"])

@router.get("/", response_model=List[schemas.ProdutoOut])
def list_produtos():
    """ lista todos os produtos """
    service = ProdutoService()
    return service.get_all_produtos()
#
@router.get("/{id}/", response_model=Optional[schemas.ProdutoOut])
def get_produto_by_id(id: int):
    """ busca um produto por ID """
    service = ProdutoService()
    return service.get_produto_by_id(id)

@router.post("/", response_model=schemas.Produto, status_code=201)
def add_produto(p: schemas.ProdutoCreate):
    """ insere um novo produto """
    service = ProdutoService()
    return service.create_produto(p)