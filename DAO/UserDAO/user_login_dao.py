from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError

from Model import User
from .user_dao import UserDAO


class UserLoginDAO(UserDAO):
    """"""

    async def read_user_by_username(self, username: str) -> User | None:
        """"""
        query = select(User).where(User.username.__eq__(username))

        try:
            async with self._session_maker() as session:
                result = await session.execute(query)
                user = result.fetchone()

        except SQLAlchemyError as e:
            raise Exception(str(e))

        return user[0]

    async def read_user_by_email(self, email: str) -> User | None:
        """"""
        query = select(User).where(User.email.__eq__(email))

        try:
            async with self._session_maker() as session:
                result = await session.execute(query)
                user = result.fetchone()

        except SQLAlchemyError as e:
            raise Exception(str(e))

        return user[0]