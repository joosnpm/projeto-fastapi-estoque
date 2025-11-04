from . import schemas
from .repository import EstoqueRepository

class EstoqueService:
    
    def get_all_estoque(self):
        repository = EstoqueRepository()
        return repository.get_all()

    def get_estoque_by_id(self, id: int):
        repository = EstoqueRepository()
        return repository.get_id(id)

    def create_estoque(self, e: schemas.EstoqueCreate):
        # Aqui você poderia validar se o produto_id existe,
        # ou se já existe um estoque para esse produto (se a regra for 1-para-1)
        repository = EstoqueRepository()
        return repository.save(e)