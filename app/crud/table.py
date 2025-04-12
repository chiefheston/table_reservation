from app.crud.base import CRUDBase
from app.models import Table


class CRUDTable(CRUDBase):
    pass



table_crud = CRUDTable(Table)
