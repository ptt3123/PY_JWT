from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from config import settings


class AsyncSessionProviderService:
    def __init__(self):
        self._engine = async_engine = create_async_engine(
            settings.DATABASE_URL, echo=False, future=True)
        self._session_maker = async_sessionmaker(
            bind=async_engine,autoflush=True,autocommit=False,expire_on_commit=False)

    async def get_session(self) -> AsyncSession:
        async with self._session_maker() as session:
            return session