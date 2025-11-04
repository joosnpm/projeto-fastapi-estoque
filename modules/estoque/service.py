from . import schemas
from .repository import EstoqueRepository

class EstoqueService:
    
    def get_all_estoque(self):
        repository = EstoqueRepository()
        return repository.get_all()

    def get_estoque_by_id(self, id: int):
        repository = EstoqueRepository()
        return repository.get_id(id)
#
    def create_estoque(self, e: schemas.EstoqueCreate):
        repository = EstoqueRepository()
        return repository.save(e)