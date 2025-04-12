from app.validators.base import BaseValidator
from app.models import Table

class TableValidator(BaseValidator):
    pass

table_validator = TableValidator(Table)