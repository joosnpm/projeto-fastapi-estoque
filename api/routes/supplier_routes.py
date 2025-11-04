from typing import Optional, List
from fastapi import APIRouter
from modules.supplier import schemas
from modules.supplier.service import SupplierService

router = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])

@router.get("/", response_model=List[schemas.Supplier])
def list_suppliers():
    """ lista todos os fornecedores """
    service = SupplierService()
    return service.get_all_suppliers()

@router.get("/{id}/", response_model=Optional[schemas.Supplier])
def get_supplier_by_id(id: int):
    """ busca um fornecedor por id """
    service = SupplierService()
    return service.get_supplier_by_id(id)
#
@router.post("/", response_model=schemas.Supplier, status_code=201)
def add_supplier(sp: schemas.SupplierCreate):
    """ insere um novo fornecedor """
    service = SupplierService()
    return service.create_supplier(sp)