from Service.RequestLimitService import (RequestLimitService,
                                         RequestLimitByIPService)
from config import settings


login_limit_by_ip_service = RequestLimitByIPService(
    settings.MAX_LOGIN_PER_IP, settings.MINUTES_LOCK_LOGIN_PER_IP)


async def get_login_limit_by_ip_service() -> RequestLimitService:
    """
    Get login_limit_by_ip_service (Global Instance Of :class:`RequestLimitByIPService` For Limit Login Request)

    :return: (:class:`RequestLimitService`)
    """

    return login_limit_by_ip_service