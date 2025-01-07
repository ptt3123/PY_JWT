from Service.RateLimitService import RateLimitAdvancedService
from config import settings


login_limit_by_ip_service = RateLimitAdvancedService(
    settings.MAX_LOGIN_REQUEST_PER_WINDOW_BY_IP,
    settings.SECONDS_PER_WINDOW_FOR_LOGIN_REQUEST_BY_IP
)


async def get_login_limit_by_ip_service() -> RateLimitAdvancedService:

    """
    Get login_limit_by_ip_service

    :return: (:class:`RateLimitService`)
    """

    return login_limit_by_ip_service