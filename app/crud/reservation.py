from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Reservation


class CRUDReservation(CRUDBase):
    async def get_all_by_table_id(
        self,
        table_id: int,
        session: AsyncSession,
    ) -> list[Reservation]:
        reservations = await session.execute(
            select(self.model).where(
                self.model.table_id == table_id,
            )
        )
        return reservations.scalars().all()


reservation_crud = CRUDReservation(Reservation)
