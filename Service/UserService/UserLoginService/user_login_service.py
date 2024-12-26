from abc import abstractmethod

from Model import User
from DAO.UserDAO import UserLoginDAO
from Service.UserService import UserService


class UserLoginService(UserService):
    """"""

    def __init__(self, user_login_dao: UserLoginDAO):
        self._user_login_dao = user_login_dao

    @abstractmethod
    async def authenticate(self, identifier: str, password: str) -> User | None:
        pass