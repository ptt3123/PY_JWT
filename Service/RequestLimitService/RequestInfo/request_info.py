from abc import ABC, abstractmethod
from datetime import datetime, timezone


class RequestInfo(ABC):

    """
    Abstract Class Contain Info About Request Of User Or Host.

    Properties:

    - _request_count (int): Count Of User Or Host's Request.
    - _last_request (datetime): Time Of Last User Or Host's Request.

    Functions:

    - check: Check If User Or Host Can Request More And Update Or Reset Info
    - update: Update Info Of User Or Host
    - reset: Reset Info Of User Or Host
    """

    _request_count: int
    _last_request: datetime

    def __init__(self):
        self._request_count = 1
        self._last_request = datetime.now(timezone.utc)

    @abstractmethod
    async def check(self, minutes_block: int, max_count: int) -> bool:
        """ Check If User Or Host Can Send Request More Or Not """
        pass

    @abstractmethod
    async def update(self, now: datetime) -> None:
        """ Update Info """
        pass

    @abstractmethod
    async def reset(self, now: datetime) -> None:
        """ Reset Info """
        pass