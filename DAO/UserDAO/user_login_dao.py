from sqlalchemy.future import select

from Model import User
from .user_dao import UserDAO


class UserLoginDAO(UserDAO):

    """
    User DAO For Log in

    Functions:

    - ``read_user_by_username``
    - ``read_user_by_email``
    """

    async def read_user_by_username(self, username: str) -> User | None:
        """
        Read User By Username

        :param username: (:class:`str`)
        :return: (:class:`User`)
        """

        query = select(User).where(User.username.__eq__(username))
        result = await self.execute_with_select(query)
        user = result.fetchone()
        return user[0]

    async def read_user_by_email(self, email: str) -> User | None:
        """
        Read User By Email

        :param email: (:class:`str`)
        :return: (:class:`User`)
        """

        query = select(User).where(User.email.__eq__(email))
        result = await self.execute_with_select(query)
        user = result.fetchone()
        return user[0]