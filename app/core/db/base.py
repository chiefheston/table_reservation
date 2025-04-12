import caseconverter

from app.core.config import settings

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db_naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls):
        return str(caseconverter.snakecase(cls.__name__))

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )
