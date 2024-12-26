from datetime import datetime, timezone, timedelta
from .login_info import LoginInfo


class LoginBaseInfo(LoginInfo):
    """Login Info Just Have Info About Login Count And Last Login Time"""

    async def check(self, minutes_block: int, max_count: int) -> bool:
        """ Check If User Or Host Can Log in:

                1, If Now >= Last Login + Minutes Block -> Reset Info And Return True

                2, Else If Login Count < Max Count -> Update Info And Return True

                3, Else Return False
        """

        now = datetime.now(timezone.utc)
        if now - self._last_login >= timedelta(minutes=minutes_block):
            await self.reset(now)
            return True

        else:
            if self._login_count < max_count:
                await self.update(now)
                return True

        return False

    async def update(self, now: datetime) -> None:
        """ Update Info:

                1, _login_count Increased By 1

                2, _last_login Assigned By Now
        """

        self._login_count += 1
        self._last_login = now

    async def reset(self, now: datetime) -> None:
        """ Update Info:

                1, _login_count Assigned By 1

                2, _last_login Assigned By Now
        """

        self._login_count = 1
        self._last_login = now