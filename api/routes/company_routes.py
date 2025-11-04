from typing import List
from modules.produto import schemas as produto_schemas
from modules.produto.service import ProdutoService as ProdutoService
from typing import Optional

from fastapi import APIRouter

from modules.company import schemas
from modules.company.schemas import CompanyCreate
from modules.company.service import CompanyService

# from app.modules.company import service, schemas

router = APIRouter(prefix="/company", tags=["Company"])


@router.get("/", response_model=list[schemas.Company])
def list_companies():
    service = CompanyService()
    return service.get_companies()
    # return service.get_companies()


@router.get("/{id}/", response_model=Optional[schemas.Company])
def get_company_by_id(id: int):
    service = CompanyService()
    return service.get_company_id(id)


@router.post("/", response_model=schemas.Company)
def add_company(company: CompanyCreate):
    service = CompanyService()
    return service.create_company(company)


@router.get("/{id}/produtos/", response_model=List[produto_schemas.ProdutoOut])
def get_company_produtos(id: int):
    """ Lista todos os produtos de uma empresa específica """
    service = ProdutoService()
    return service.get_produtos_by_company(id)