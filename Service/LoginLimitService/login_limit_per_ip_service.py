from config import settings
from .LoginInfo import LoginBaseInfo
from .login_limit_service import LoginLimitService


class LoginLimitPerIPService(LoginLimitService):
    """"""
    _instance = None
    _max_count: int
    _minutes_block: int
    _data: dict[str, LoginBaseInfo]

    def __new__(cls):
        """ Singleton Pattern """
        if cls._instance is None:
            cls._instance = super(LoginLimitService, cls).__new__(cls)
            cls._instance._max_count = settings.MAX_LOGIN_PER_IP
            cls._instance._minutes_block = settings.MINUTES_LOCK_LOGIN_PER_IP
            cls._instance._data = {}

        return cls._instance

    async def add(self, user: str) -> None:
        """ Add Data """
        self._data.update({user: LoginBaseInfo()})

    async def check(self, user: str) -> bool:
        """ Check If User Or Host Can Log In More """
        if not self._data.__contains__(user):
            await self.add(user)
            return True

        return await self._data.get(user).check(self._minutes_block, self._max_count)