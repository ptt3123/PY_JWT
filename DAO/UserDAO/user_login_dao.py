from sqlalchemy.future import select

from Model import User
from .user_dao import UserDAO


class UserLoginDAO(UserDAO):
    """"""

    async def read_user_by_username(self, username: str) -> User | None:
        """"""
        query = select(User).where(User.username.__eq__(username))
        result = await self.execute_with_select(query)
        user = result.fetchone()
        return user[0]

    async def read_user_by_email(self, email: str) -> User | None:
        """"""
        query = select(User).where(User.email.__eq__(email))
        result = await self.execute_with_select(query)
        user = result.fetchone()
        return user[0]