from typing import Optional, List
from fastapi import APIRouter
from modules.estoque import schemas
from modules.estoque.service import EstoqueService

router = APIRouter(prefix="/estoque", tags=["Estoque"])

@router.get("/", response_model=List[schemas.EstoqueOut])
def list_estoque():
    """ lista todos os registros de estoque com o nome do produto """
    service = EstoqueService()
    return service.get_all_estoque()
#
@router.get("/{id}/", response_model=Optional[schemas.EstoqueOut])
def get_estoque_by_id(id: int):
    """ busca um registro de estoque por id com o nome do produto """
    service = EstoqueService()
    return service.get_estoque_by_id(id)

@router.post("/", response_model=schemas.EstoqueOut, status_code=201)
def add_estoque(e: schemas.EstoqueCreate):
    """ insere um novo registro de estoque """
    service = EstoqueService()
    return service.create_estoque(e)