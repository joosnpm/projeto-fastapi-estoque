from . import schemas
from .repository import TypeProductRepository

class TypeProductService:
    
    def get_all_types(self):
        repository = TypeProductRepository()
        return repository.get_all()

    def get_type_by_id(self, id: int):
        repository = TypeProductRepository()
        return repository.get_id(id)

    def create_type(self, tp: schemas.TypeProductCreate):
        # Aqui você poderia adicionar validações (ex: se o 'cod' já existe)
        repository = TypeProductRepository()
        return repository.save(tp)