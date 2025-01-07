import time


class RateLimitService:

    """
     Rate Limit Service By Using Fixed Window

    Properties:

    - ``_max_request_per_window``: (:class:`int`)
    - ``_minutes_per_window``: (:class:`int`)
    - ``_request``: (:class:`int`)
    - ``_last_window``: (:class:`int`)

    Abstract Methods:

    - ``check_if_can_execute_request`` -> (:class:`bool`)
    - ``update_info`` -> (:class:`None`)
    - ``reset_info`` -> (:class:`None`)
    """

    _max_request_per_window: int
    _minutes_per_window: int
    _request: int
    _last_window: int

    def __init__(self, max_request: int, minutes_per_window: int):
        self._max_request = max_request
        self._minutes_per_window = minutes_per_window
        self._request = 0
        self._last_window = 0

    async def check_if_can_execute_request(self) -> bool:

        """
        Check If Server Can Execute More Request

        :return: (:class:`bool`)
        """

        current_time = int(time.time())
        now_window = current_time // self._minutes_per_window

        if self._last_window < now_window:
            await self.reset_info(now_window)
            return True

        if self._request < self._max_request:
            await self.update_info()
            return True

        return False

    async def update_info(self) -> None:

        """
        Increase _request by 1

        :return: (:class:`None`)
        """

        self._request += 1

    async def reset_info(self, now_window: int) -> None:

        """
        Increase _request by 1, And Update _last_window By Now Window

        :param now_window: (:class:`int`) Now Window
        :return: (:class:`None`)
        """

        self._request = 1
        self._last_window = now_window