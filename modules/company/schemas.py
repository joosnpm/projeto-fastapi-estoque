from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name: str
    cnpj: str
    status: str

class Company(BaseModel):
    id: int
    name: str
    cnpj: str
    status: str
    
    class Config:
        from_attributes = True