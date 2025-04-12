from app.core.db import Base

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Table(Base):
    name: Mapped[str] = mapped_column(
        String(55),
        unique=True,
    )
    seats: Mapped[int] = mapped_column(Integer)
    location: Mapped[String] = mapped_column(String(140))
