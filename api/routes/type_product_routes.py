from typing import Optional, List
from fastapi import APIRouter
from modules.type_product import schemas
from modules.type_product.service import TypeProductService

router = APIRouter(prefix="/tipo", tags=["Tipo"])

@router.get("/", response_model=List[schemas.TypeProduct])
def list_types():
    """ lista todos os tipos de produto """
    service = TypeProductService()
    return service.get_all_types()

@router.get("/{id}/", response_model=Optional[schemas.TypeProduct])
def get_type_by_id(id: int):
    """ busca um tipo de produto por id """
    service = TypeProductService()
    return service.get_type_by_id(id)
#
@router.post("/", response_model=schemas.TypeProduct, status_code=201)
def add_type(tp: schemas.TypeProductCreate):
    """ insere um novo tipo de produto """
    service = TypeProductService()
    return service.create_type(tp)