from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

from exception import TOO_MUCH_LOGIN_REQUEST_EXCEPTION
from Service.RateLimitService import RateLimitAdvancedService
from ..ServiceDependency import (
    get_login_limit_by_ip_service, get_login_limit_by_identifier_service)


async def login_limit_dependency(
        request: Request,
        user_form: OAuth2PasswordRequestForm = Depends(),
        login_limit_by_ip_service: RateLimitAdvancedService =
        Depends(get_login_limit_by_ip_service),
        login_limit_by_identifier_service: RateLimitAdvancedService =
        Depends(get_login_limit_by_identifier_service),
) \
        -> None:

    ip = request.state.client_ip
    if not await login_limit_by_ip_service.check(ip):
        # Soft Limit With CAPTCHA
        raise TOO_MUCH_LOGIN_REQUEST_EXCEPTION

    if not await login_limit_by_identifier_service.check(user_form.username):
        raise TOO_MUCH_LOGIN_REQUEST_EXCEPTION

    return