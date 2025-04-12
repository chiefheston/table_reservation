from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def get(
        self,
        obj_id: int,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(self.model.id == obj_id),
        )
        return db_obj.scalars().first()

    async def create(
        self,
        obj_in,
        session: AsyncSession,
    ):
        obj_in_dump = obj_in.model_dump()
        db_obj = self.model(**obj_in_dump)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
        self,
        db_obj,
        session: AsyncSession,
    ):
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_all(
        self,
        session: AsyncSession,
    ):
        db_objs = await session.execute(
            select(self.model),
        )
        return db_objs.scalars().all()

    async def get_id_by_name(
        self,
        name: str,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(self.model.name == name),
        )
        return db_obj.scalars().first()
