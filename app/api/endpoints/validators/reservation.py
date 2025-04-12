from datetime import datetime, timedelta
from http import HTTPStatus

from app.api.endpoints.validators.base import BaseValidator
from app.crud import reservation_crud
from app.models import Reservation
from app.services.constants import (
    ERR_DATETIME_FORMAT,
    ERR_RESERVATION_OVERLAPPING,
)
from app.services.reservation import get_overlapping_reservations

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


class ReservationValidator(BaseValidator):
    async def check_datetime(self, datetime: datetime) -> None:
        if datetime.tzinfo is not None:
            raise HTTPException(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                detail=ERR_DATETIME_FORMAT,
            )

    async def check_reservation_intersections(
        self,
        reservation: Reservation,
        session: AsyncSession,
    ) -> None:
        reservation_list = await reservation_crud.get_all_by_table_id(
            table_id=reservation.table_id,
            session=session,
        )

        start_time = reservation.reservation_time  # Reservation start time
        delta = timedelta(minutes=reservation.duration_minutes)
        end_time = start_time + delta  # Reservation end time

        overlapping_reservations = await get_overlapping_reservations(
            reservations_list=reservation_list,
            reservation_start_time=start_time,
            reservation_end_time=end_time,
        )

        if overlapping_reservations:
            raise HTTPException(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                detail=ERR_RESERVATION_OVERLAPPING.format(
                    overlapping_reservations,
                ),
            )


reservation_validator = ReservationValidator(Reservation)
