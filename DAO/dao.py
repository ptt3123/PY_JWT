from abc import ABC
from database import async_session_maker
from sqlalchemy.ext.asyncio import async_sessionmaker


class DAO(ABC):
    """"""

    def __init__(self):
        self._session_maker: async_sessionmaker = async_session_maker
