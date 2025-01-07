from Service.RateLimitService import RateLimitAdvancedService
from config import settings

login_limit_by_identifier_service = RateLimitAdvancedService(
    settings.MAX_LOGIN_REQUEST_PER_WINDOW_BY_IDENTIFIER,
    settings.SECONDS_PER_WINDOW_FOR_LOGIN_REQUEST_BY_IDENTIFIER
)


async def get_login_limit_by_identifier_service() -> RateLimitAdvancedService:
    """
    Get login_limit_by_username_service

    :return: (:class:`RateLimitService`)
    """

    return login_limit_by_identifier_service