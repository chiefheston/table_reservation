from http import HTTPStatus

from app.core.db import db_helper
from app.crud.table import table_crud
from app.schemas.table import (
    TableCreate,
    TableDelete,
    TableRead,
)
from app.validators import reservation_validator, table_validator

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/tables",
    tags=["Tables"],
)


@router.get(
    "/",
    response_model=list[TableRead],
)
async def get_all_tables(
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    return await table_crud.get_all(session)


@router.post(
    "/",
    response_model=TableCreate,
    status_code=HTTPStatus.CREATED,
)
async def create_table(
    table: TableCreate,
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    await table_validator.name_exists(table.name, session)
    return await table_crud.create(table, session)


@router.delete(
    "/{table_id}",
    response_model=TableDelete,
)
async def delete_table(
    table_id: int,
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    table = await table_validator.object_exists(
        table_id,
        session,
    )
    await reservation_validator.check_reservations_by_table(
        table_id=table_id,
        session=session,
    )
    return await table_crud.remove(
        table,
        session,
    )
