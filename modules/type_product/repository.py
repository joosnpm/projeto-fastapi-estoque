from core.db import DataBase
from .schemas import TypeProductCreate

class TypeProductRepository:
    QUERY_GET_ALL = "SELECT id, name, cod, company_id FROM type_product"
    QUERY_GET_BY_ID = "SELECT id, name, cod, company_id FROM type_product WHERE id = %s"
    QUERY_CREATE = "INSERT INTO type_product (name, cod, company_id) VALUES (%s, %s, %s) RETURNING id, name, cod, company_id;"

    def get_all(self):
        db = DataBase()
        results_db = db.execute(self.QUERY_GET_ALL)
        results = []
        for row in results_db:
            results.append({"id": row[0], "name": row[1], "cod": row[2], "company_id": row[3]})
        return results

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_GET_BY_ID % id
        row = db.execute(query, many=False)
        if row:
            return {"id": row[0], "name": row[1], "cod": row[2], "company_id": row[3]}
        return None
#
    def save(self, tp: TypeProductCreate):
        db = DataBase()
        query = self.QUERY_CREATE % (f"'{tp.name}'", f"'{tp.cod}'", tp.company_id)
        row = db.commit(query)
        return {"id": row[0], "name": row[1], "cod": row[2], "company_id": row[3]}