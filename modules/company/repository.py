from core.db import DataBase
from modules.company.schemas import CompanyCreate


class CompanyRepository:

    QUERY_COMPANIES = "SELECT id, name, cnpj, status FROM company"
    

    QUERY_COMPANY_ID = "SELECT id, name, cnpj, status FROM company WHERE id = %s"
    

    QUERY_CREATE_COMPANY = "INSERT INTO company (name, cnpj, status) VALUES (%s, %s, %s) RETURNING id, name, cnpj, status;"

    def _map_row_to_company(self, row):

        return {"id": row[0], "name": row[1], "cnpj": row[2], "status": row[3]}

    def get_all(self):
        db = DataBase()
        companies = db.execute(self.QUERY_COMPANIES)

        return [self._map_row_to_company(row) for row in companies]

    def save(self, company: CompanyCreate):
        db = DataBase()
    
        query = self.QUERY_CREATE_COMPANY % (
            f"'{company.name}'",
            f"'{company.cnpj}'",
            f"'{company.status}'"
        )
        result = db.commit(query)
    
        return self._map_row_to_company(result)
#
    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_COMPANY_ID % id
        company = db.execute(query, many=False)
        if company:
            
            return self._map_row_to_company(company)
        return None