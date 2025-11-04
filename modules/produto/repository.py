from core.db import DataBase
from .schemas import ProdutoCreate

class ProdutoRepository:
    
    # Query com join para buscar nomes do tipo e fornecedor
    QUERY_GET_ALL = """
        SELECT 
            p.id, p.name, p.price, p.company_id,
            tp.name as type_name, 
            s.name as supplier_name
        FROM produto p
        INNER JOIN type_product tp ON p.type_id = tp.id
        INNER JOIN supplier s ON p.supplier_id = s.id
    """
    
    # Query com join para buscar um produto
    QUERY_GET_BY_ID = """
        SELECT 
            p.id, p.name, p.price, p.company_id,
            tp.name as type_name, 
            s.name as supplier_name
        FROM produto p
        INNER JOIN type_product tp ON p.type_id = tp.id
        INNER JOIN supplier s ON p.supplier_id = s.id
        WHERE p.id = %s
    """
    
    # Query simples para criar
    QUERY_CREATE = "INSERT INTO produto (name, description, price, type_id, supplier_id, company_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id, name, description, price, type_id, supplier_id, company_id;"

    # Query para buscar produtos da empresa
    QUERY_GET_BY_COMPANY = """
        SELECT 
            p.id, p.name, p.price, p.company_id,
            tp.name as type_name, 
            s.name as supplier_name
        FROM produto p
        INNER JOIN type_product tp ON p.type_id = tp.id
        INNER JOIN supplier s ON p.supplier_id = s.id
        WHERE p.company_id = %s
    """

    def _map_row_to_out(self, row):
        return {"id": row[0], "name": row[1], "price": row[2], "company_id": row[3], "type_name": row[4], "supplier_name": row[5]}

    def get_all(self):
        db = DataBase()
        results_db = db.execute(self.QUERY_GET_ALL)
        return [self._map_row_to_out(row) for row in results_db]

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_GET_BY_ID % id
        row = db.execute(query, many=False)
        if row:
            return self._map_row_to_out(row)
        return None

    def get_by_company_id(self, company_id: int):
        db = DataBase()
        query = self.QUERY_GET_BY_COMPANY % company_id
        results_db = db.execute(query)
        return [self._map_row_to_out(row) for row in results_db]
#
    def save(self, p: ProdutoCreate):
        db = DataBase()
        query = self.QUERY_CREATE % (
            f"'{p.name}'", f"'{p.description}'", p.price, p.type_id, p.supplier_id, p.company_id
        )
        row = db.commit(query)
        # Retorna o produto sem os joins
        return {"id": row[0], "name": row[1], "description": row[2], "price": row[3], "type_id": row[4], "supplier_id": row[5], "company_id": row[6]}