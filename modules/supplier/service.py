from . import schemas
from .repository import SupplierRepository

class SupplierService:
    
    def get_all_suppliers(self):
        repository = SupplierRepository()
        return repository.get_all()

    def get_supplier_by_id(self, id: int):
        repository = SupplierRepository()
        return repository.get_id(id)
#
    def create_supplier(self, sp: schemas.SupplierCreate):
        repository = SupplierRepository()
        return repository.save(sp)