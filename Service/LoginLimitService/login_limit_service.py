from abc import ABC, abstractmethod

from .LoginInfo import LoginInfo


class LoginLimitService(ABC):
    """"""

    @abstractmethod
    async def add(self, user) -> None:
        """ Add Data """
        pass

    @abstractmethod
    async def check(self, user) -> bool:
        """ Check If User Or Host Can Log In More """
        pass