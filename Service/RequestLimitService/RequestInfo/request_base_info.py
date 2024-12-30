from datetime import datetime, timezone, timedelta

from .request_info import RequestInfo


class RequestBaseInfo(RequestInfo):
    """
    Class Contain Info About Request Of User Or Host,
    Just Contain All Properties And Functions Of :class:`RequestInfo`.
    """

    async def check(self, minutes_block: int, max_count: int) -> bool:
        """ Check If User Or Host Can Request And Update Or Reset Info:

                1, If Now >= Last Request + Minutes Block -> Reset Info And Return True

                2, Else If Request Count < Max Count -> Update Info And Return True

                3, Else Return False
        """

        now = datetime.now(timezone.utc)
        if now - self._last_request >= timedelta(minutes=minutes_block):
            await self.reset(now)
            return True

        else:
            if self._request_count < max_count:
                await self.update(now)
                return True

        return False

    async def update(self, now: datetime) -> None:
        """ Update Info:

                1, _request_count Increased By 1

                2, _last_request Assigned By Now
        """

        self._request_count += 1
        self._last_request = now

    async def reset(self, now: datetime) -> None:
        """ Update Info:

                1, _request_count Assigned By 1

                2, _last_request Assigned By Now
        """

        self._request_count = 1
        self._last_request = now