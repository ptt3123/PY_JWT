from ..RequestInfo import RequestBaseInfo
from ..request_limit_service import RequestLimitService


class RequestLimitByIPService(RequestLimitService):

    """
    Request Limit By Ip Service, Deployment All Of :class:`RequestLimitService`

    Properties: Like RequestLimitService, But Value Of _data is :class:`RequestBaseInfo`, Not :class:`RequestInfo`

    Functions: Just Like RequestLimitService, With Key user Is IP Of Host
    """

    def __init__(self, max_count: int, minutes_block: int):
        self._max_count = max_count
        self._minutes_block = minutes_block
        self._data = {}

    async def add(self, user: str) -> None:
        """ Add Info About IP """
        self._data.update({user: RequestBaseInfo()})

    async def check(self, user: str) -> bool:
        """
        Check If Host Can Request More And Update Info

        If _data Contain IP Of Host, Call Add
        """
        if not self._data.__contains__(user):
            await self.add(user)
            return True

        return await self._data.get(user).check(self._minutes_block, self._max_count)