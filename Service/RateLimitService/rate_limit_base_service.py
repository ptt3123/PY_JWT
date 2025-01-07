from CustomType.RequestInfo import RequestInfo
from .rate_limit_service import RateLimitService


class RateLimitBaseService(RateLimitService):
    """"""

    _info: RequestInfo

    def __init__(self, max_request_per_window: int, seconds_per_window: int):
        super().__init__(max_request_per_window, seconds_per_window)
        self._info = RequestInfo(self._seconds_per_window)

    async def check(self) -> bool:
        """"""

        return await self._info.check(
            self._max_request_per_window, self._seconds_per_window
        )