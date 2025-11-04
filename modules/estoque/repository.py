from core.db import DataBase
from .schemas import EstoqueCreate

class EstoqueRepository:
     
     # Query com join para buscar o nome do produto
    QUERY_GET_ALL = """
        SELECT 
            e.id, e.quantidade, e.data_atualizacao, e.produto_id,
            p.name as produto_name
        FROM estoque e
        INNER JOIN produto p ON e.produto_id = p.id
    """
    
    # Query com join para buscar um produto
    QUERY_GET_BY_ID = """
        SELECT 
            e.id, e.quantidade, e.data_atualizacao, e.produto_id,
            p.name as produto_name
        FROM estoque e
        INNER JOIN produto p ON e.produto_id = p.id
        WHERE e.id = %s
    """
    
    # Query simples para criar.
    QUERY_CREATE = "INSERT INTO estoque (produto_id, quantidade) VALUES (%s, %s) RETURNING id, produto_id, quantidade, data_atualizacao;"

    def _map_row_to_out(self, row):
        # Mapeia o resultado do banco 
        return {"id": row[0], "quantidade": row[1], "data_atualizacao": row[2], "produto_id": row[3], "produto_name": row[4]}

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

    def save(self, e: EstoqueCreate):
        db = DataBase()
        query = self.QUERY_CREATE % (e.produto_id, e.quantidade)
        row = db.commit(query)
        
        return self.get_id(row[0])