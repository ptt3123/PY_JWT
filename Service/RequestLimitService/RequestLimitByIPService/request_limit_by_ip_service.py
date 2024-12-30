from ..RequestInfo import RequestBaseInfo
from ..request_limit_service import RequestLimitService


class RequestLimitByIPService(RequestLimitService):
    """"""
    _max_count: int
    _minutes_block: int
    _data: dict[str, RequestBaseInfo]

    def __init__(self, max_count: int, minutes_block: int):
        self._max_count = max_count
        self._minutes_block = minutes_block
        self._data = {}

    async def add(self, user: str) -> None:
        """ Add Info About IP """
        self._data.update({user: RequestBaseInfo()})

    async def check(self, user: str) -> bool:
        """ Check If Host Can Request More And Update Info """
        if not self._data.__contains__(user):
            await self.add(user)
            return True

        return await self._data.get(user).check(self._minutes_block, self._max_count)