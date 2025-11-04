from typing import Optional, List
from fastapi import APIRouter
from modules.produto import schemas
from modules.produto.service import ProdutoService

router = APIRouter(prefix="/produto", tags=["Produto"])

@router.get("/", response_model=List[schemas.ProdutoOut])
def list_produtos():
    """ Lista todos os produtos (com nomes de tipo e fornecedor) """
    service = ProdutoService()
    return service.get_all_produtos()

@router.get("/{id}/", response_model=Optional[schemas.ProdutoOut])
def get_produto_by_id(id: int):
    """ Busca um produto por ID (com nomes de tipo e fornecedor) """
    service = ProdutoService()
    return service.get_produto_by_id(id)

@router.post("/", response_model=schemas.Produto, status_code=201)
def add_produto(p: schemas.ProdutoCreate):
    """ Insere um novo produto (retorna o produto simples) """
    service = ProdutoService()
    return service.create_produto(p)