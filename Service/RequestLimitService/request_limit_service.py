from abc import ABC, abstractmethod

from .RequestInfo import RequestInfo


class RequestLimitService(ABC):
    """
    Service Contain Info Of User Or Host's Request:

    Properties:

    - _max_count (int) : Number Of Max Request User Or Host Can Request In One Time (Minutes)
    - _minutes_block (int) : Time Block Of User Or Host When Over Request
    - _data (dict[str, RequestInfo]) : A Dict With Key (str) Define User Or Host Like IP, ID, ...And Value Is :class:`RequestInfo`

    Functions:

    - add(self, user: str) -> None : Add Info Of User With Key `user` (str)
    - check(self, user: str) -> bool: Check If User With Key `user` (str) Can Send Request More And Update Info
    """

    _max_count: int
    _minutes_block: int
    _data: dict[str, RequestInfo]

    @abstractmethod
    async def add(self, user: str) -> None:
        """ Add Data """
        pass

    @abstractmethod
    async def check(self, user: str) -> bool:
        """ Check If User Or Host Can Log In More """
        pass