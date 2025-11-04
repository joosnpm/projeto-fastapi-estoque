from pydantic import BaseModel
from datetime import datetime

class EstoqueBase(BaseModel):
    produto_id: int
    quantidade: int

class EstoqueCreate(EstoqueBase):
    pass
#
class EstoqueOut(BaseModel):
    id: int
    quantidade: int
    data_atualizacao: datetime
    produto_id: int
    produto_name: str  

    class Config:
        from_attributes = True


class Estoque(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    data_atualizacao: datetime
    
    class Config:
        from_attributes = True