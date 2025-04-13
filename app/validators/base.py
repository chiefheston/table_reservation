from http import HTTPStatus

from app.core.db import Base
from app.crud.base import CRUDBase
from app.services import constants as const

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession


class BaseValidator:
    def __init__(self, model: Base):
        self.model = model

    async def name_exists(
        self,
        obj_name: str,
        session: AsyncSession,
    ) -> None:
        """Check existing model name

        Args:
            obj_name (str): Object name
            session (AsyncSession): Session object
            model (Base): Model object

        Raises:
            HTTPException: "Name 'obj_name' is busy!"

        Returns:
            None
        """
        obj = await CRUDBase(model=self.model).get_id_by_name(
            obj_name,
            session,
        )
        if obj is not None:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail=const.ERR_NAME_BUSY.format(
                    self.model.__name__.upper(),
                    obj_name,
                ),
            )

    async def object_exists(
        self,
        obj_id: int,
        session: AsyncSession,
    ) -> None:
        """Check existing object with id.

        Args:
            obj_id (int): Object id.
            session (AsyncSession): Session object.

        Raises:
            HTTPException: Object with id 'obj_id' not found!

        Returns:
            Base: Requested object.
        """
        obj = await CRUDBase(self.model).get(
            obj_id,
            session,
        )
        if obj is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=const.ERR_OBJECT_NOT_FOUND_ID.format(
                    str(self.model.__name__).upper(),
                    obj_id,
                ),
            )

        return obj
