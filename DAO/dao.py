from abc import ABC
from typing import Type
from sqlalchemy import Select, Result
from sqlalchemy.exc import SQLAlchemyError

from database import async_session_maker, Base
from sqlalchemy.ext.asyncio import async_sessionmaker


class DAO(ABC):
    """"""

    def __init__(self):
        self._session_maker: async_sessionmaker = async_session_maker

    async def execute_with_select(self, query: Select) -> Result:
        try:
            async with self._session_maker() as session:
                result = await session.execute(query)

        except SQLAlchemyError as e:
            raise Exception(str(e))

        return result

    async def execute_with_add(self, model: Type[Base]) -> Type[Base]:
        try:
            async with self._session_maker() as session:
                session.add(model)
                await session.commit()
                await session.refresh(model)

        except SQLAlchemyError as e:
            await session.rollback()
            raise Exception(str(e))

        return model