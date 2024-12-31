from fastapi import Depends, Request

from exception import TOO_MUCH_LOGIN_REQUEST_EXCEPTION
from Service.RequestLimitService import RequestLimitService
from ..ServiceDependency import get_login_limit_by_ip_service

async def login_limit_dependency(
        request: Request,
        login_limit_service: RequestLimitService = Depends(get_login_limit_by_ip_service)) \
        -> None:

    """
    Check If User Or Host Can Log In More Or Not

    If Not Raise Exception, Else Return None

    :param request: (:class:`Request`)
    :param login_limit_service: (:class:`RequestLimitService`)
    :return: (:class:`None`)
    """

    if not await login_limit_service.check(request.client.host):
        raise TOO_MUCH_LOGIN_REQUEST_EXCEPTION

    return