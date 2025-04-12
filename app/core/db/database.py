from app.core.config import settings
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


class DBHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_maker = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    async def get_async_session(self):
        async with self.session_maker() as session:
            yield session


db_helper = DBHelper(
    url=str(settings.db_url),
    echo=settings.db_echo,
)
