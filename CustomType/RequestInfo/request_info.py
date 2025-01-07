import time


class RequestInfo:
    """"""

    _request_count: int
    _current_window: int

    def __init__(self, window: int):
        current_time = int(time.time())
        current_window = current_time // window

        self._request_count = 1
        self._current_window = current_window

    async def check(self, max_request: int, window : int) -> bool:
        """
        Check If User Or Host Can Send Request More Or Not

        :param max_request:
        :param window:
        :return:
        """

        current_time = int(time.time())
        current_window = current_time // window

        if self._current_window < current_window:
            await self.reset(current_window)
            return True

        if self._request_count < max_request:
            await self.update()
            return True

        return False

    async def update(self) -> None:
        """
        Update Request Count

        :return: (None)
        """

        self._request_count += 1

    async def reset(self, current_window : int) -> None:
        """
        Reset Request To 1 And Last Window To ``current_window``

        :param current_window:
        :return: (None)
        """

        self._request_count = 1
        self._current_window = current_window