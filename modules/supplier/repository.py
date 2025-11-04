from core.db import DataBase
from .schemas import SupplierCreate

class SupplierRepository:
    QUERY_GET_ALL = "SELECT id, name, cnpj, status, company_id FROM supplier"
    QUERY_GET_BY_ID = "SELECT id, name, cnpj, status, company_id FROM supplier WHERE id = %s"
    QUERY_CREATE = "INSERT INTO supplier (name, cnpj, status, company_id) VALUES (%s, %s, %s, %s) RETURNING id, name, cnpj, status, company_id;"

    def get_all(self):
        db = DataBase()
        results_db = db.execute(self.QUERY_GET_ALL)
        results = []
        for row in results_db:
            results.append({"id": row[0], "name": row[1], "cnpj": row[2], "status": row[3], "company_id": row[4]})
        return results
#
    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_GET_BY_ID % id
        row = db.execute(query, many=False)
        if row:
            return {"id": row[0], "name": row[1], "cnpj": row[2], "status": row[3], "company_id": row[4]}
        return None

    def save(self, sp: SupplierCreate):
        db = DataBase()
        query = self.QUERY_CREATE % (f"'{sp.name}'", f"'{sp.cnpj}'", f"'{sp.status}'", sp.company_id)
        row = db.commit(query)
        return {"id": row[0], "name": row[1], "cnpj": row[2], "status": row[3], "company_id": row[4]}