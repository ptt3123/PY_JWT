from CustomType.RequestInfo import RequestInfo
from .rate_limit_service import RateLimitService


class RateLimitAdvancedService(RateLimitService):
    """"""

    _info: dict[str, RequestInfo]

    def __init__(self, max_request_per_window: int, seconds_per_window: int):
        super().__init__(max_request_per_window, seconds_per_window)
        self._info = {}

    async def check(self, key: str) -> bool:
        """"""

        request_info = self._info.get(key)
        if not request_info:
            await self.add_info(key)
            return True

        return await request_info.check(
            self._max_request_per_window, self._seconds_per_window
        )

    async def add_info(self, key: str):
        """"""

        self._info.update({key: RequestInfo(self._seconds_per_window)})