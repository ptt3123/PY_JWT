from fastapi import APIRouter, Request, Depends, Body

from Schema.UserSchema import UserLoginSchema
from Dependency.ServiceDependency import (get_login_service,
                                          get_login_limit_by_ip_service)
from exception import (USER_NOT_FOUND_EXCEPTION,
                       TOO_MUCH_LOGIN_REQUEST_EXCEPTION)
from Service.JWTService import AccessTokenCreatorService


login_router = APIRouter()


@login_router.post("/login")
async def login(request: Request, method: str, user: UserLoginSchema = Body(),
                login_limit_service = Depends(get_login_limit_by_ip_service),
                login_service = Depends(get_login_service),
                token_creator_service: AccessTokenCreatorService = Depends()):
    """ Return TokenBaseDTO """

    if not await login_limit_service.check(request.client.host):
        raise TOO_MUCH_LOGIN_REQUEST_EXCEPTION

    user = await login_service.authenticate(user.identifier, user.password)
    if not user:
        raise USER_NOT_FOUND_EXCEPTION

    return await token_creator_service.create_token_base(
        {"uid": user.id, "iac": user.is_active, "isf": user.is_staff}
    )