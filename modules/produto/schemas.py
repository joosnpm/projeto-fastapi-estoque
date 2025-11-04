from pydantic import BaseModel

class ProdutoBase(BaseModel):
    name: str
    description: str | None = None
    price: float  # 'preco' no seu doc, mudei para float
    type_id: int
    supplier_id: int
    company_id: int

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int

    class Config:
        from_attributes = True

# Schema especial para listagem, como pedia a DICA
class ProdutoOut(BaseModel):
    id: int
    name: str
    price: float
    company_id: int
    type_name: str         # Nome do Tipo
    supplier_name: str     # Nome do Fornecedor

    class Config:
        from_attributes = True