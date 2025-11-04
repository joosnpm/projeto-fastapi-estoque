from pydantic import BaseModel

class ProdutoBase(BaseModel):
    name: str
    description: str | None = None
    price: float  
    type_id: int
    supplier_id: int
    company_id: int

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int
#
    class Config:
        from_attributes = True

class ProdutoOut(BaseModel):
    id: int
    name: str
    price: float
    company_id: int
    type_name: str         
    supplier_name: str     

    class Config:
        from_attributes = True