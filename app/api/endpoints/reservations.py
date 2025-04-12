from http import HTTPStatus

from app.validators import reservation_validator
from app.validators import table_validator
from app.core.db import db_helper
from app.crud import reservation_crud
from app.schemas.reservation import (
    ReservationCreate,
    ReservationRead,
    ReservationDelete,
)

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"],
)


@router.get(
    "/all",
    response_model=list[ReservationRead],
    status_code=HTTPStatus.OK,
)
async def get_all_reservations(
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    return await reservation_crud.get_all(session)


@router.post(
    "/",
    response_model=ReservationCreate,
    status_code=HTTPStatus.CREATED,
)
async def create_reservation(
    reservation: ReservationCreate,
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    await table_validator.object_exists(
        obj_id=reservation.table_id,
        session=session,
    )
    await reservation_validator.check_datetime(
        datetime=reservation.reservation_time,
    )
    await reservation_validator.check_reservation_intersections(
        reservation=reservation,
        session=session,
    )
    return await reservation_crud.create(
        reservation,
        session,
    )


@router.delete(
    "/{reservation_id}",
    response_model=ReservationDelete,
    status_code=HTTPStatus.OK,
)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    reservation = await reservation_validator.object_exists(
        reservation_id,
        session,
    )
    return await reservation_crud.remove(reservation, session)
