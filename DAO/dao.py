from abc import ABC
from typing import Type
from sqlalchemy import Select, Result
from sqlalchemy.exc import SQLAlchemyError

from Service.AsyncSessionProviderService import AsyncSessionProviderService
from database import Base


class DAO(ABC):

    """
    Base DAO Class

    Property:

    - ``_session_provider_service`` (:class:`AsyncSessionProviderService`) Async Session Provider Service

    Functions (Execute Query With Try Except):

    - ``execute_with_select``
    - ``execute_with_add``
    """

    def __init__(self, session_provider_service: AsyncSessionProviderService):
        self._session_provider_service = session_provider_service

    async def execute_with_select(self, query: Select) -> Result:
        session = await self._session_provider_service.get_session()

        try:
            result = await session.execute(query)
            return result

        except SQLAlchemyError as e:
            raise e

        finally:
            await session.close()


    async def execute_with_add(self, model: Type[Base]) -> Type[Base]:
        session = await self._session_provider_service.get_session()

        try:
            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model

        except SQLAlchemyError as e:
            await session.rollback()
            raise e

        finally:
            await session.close()