from datetime import datetime

from app.core.db import Base

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Reservation(Base):
    customer_name: Mapped[str] = mapped_column(String(55))
    reservation_time: Mapped[datetime] = mapped_column(DateTime)
    duration_minutes: Mapped[int] = mapped_column(Integer)

    table_id: Mapped[int | None] = mapped_column(ForeignKey("table.id"))
