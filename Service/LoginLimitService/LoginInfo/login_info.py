from abc import ABC, abstractmethod
from datetime import datetime, timezone


class LoginInfo(ABC):
    """"""
    _login_count: int
    _last_login: datetime

    def __init__(self):
        self._login_count = 1
        self._last_login = datetime.now(timezone.utc)

    @abstractmethod
    async def check(self, minutes_block: int, max_count: int) -> bool:
        """ Check If User Or Host Can Log In Or Not """
        pass

    @abstractmethod
    async def update(self, now: datetime) -> None:
        """ Update Info """
        pass

    @abstractmethod
    async def reset(self, now: datetime) -> None:
        """ Reset Info """
        pass