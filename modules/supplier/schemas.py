from pydantic import BaseModel

class SupplierBase(BaseModel):
    name: str
    cnpj: str
    status: str
    company_id: int

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int
#
    class Config:
        from_attributes = True