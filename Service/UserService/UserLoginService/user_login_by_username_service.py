from Model import User
from ...PasswordHashingService import PasswordHashingService
from .user_login_service import UserLoginService


class UserLoginByUsernameService(UserLoginService):
    """"""

    async def authenticate(self, identifier: str, password: str) \
            -> User | None:
        """"""
        user = await self._user_login_dao.read_user_by_username(identifier)
        if not user :
            return None

        if PasswordHashingService.verify_password(password, user.password):
            return None

        return user