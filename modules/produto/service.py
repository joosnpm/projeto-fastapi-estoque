from . import schemas
from .repository import ProdutoRepository

class ProdutoService:
    
    def get_all_produtos(self):
        repository = ProdutoRepository()
        return repository.get_all()

    def get_produto_by_id(self, id: int):
        repository = ProdutoRepository()
        return repository.get_id(id)
#
    def create_produto(self, p: schemas.ProdutoCreate):
        repository = ProdutoRepository()
        return repository.save(p)
    
    def get_produtos_by_company(self, company_id: int):
        repository = ProdutoRepository()
        return repository.get_by_company_id(company_id)