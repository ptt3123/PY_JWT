from fastapi import FastAPI, Request, Depends

from DTO import TokenBaseDTO
from Dependency import get_login_service
from exception import (USER_NOT_FOUND_EXCEPTION,
                       TOO_MUCH_LOGIN_REQUEST_EXCEPTION)
from Service.LoginLimitService import LoginLimitPerIPService
from Service.JWTService import AccessTokenCreatorService


app = FastAPI()


@app.post("/login", response_model=TokenBaseDTO)
async def login(request: Request, identifier: str, password: str, method: str,
                login_limit_service = Depends(LoginLimitPerIPService),
                login_service = Depends(get_login_service),
                token_creator_service: AccessTokenCreatorService = Depends()):
    """"""

    if not await login_limit_service.check(request.client.host):
        raise TOO_MUCH_LOGIN_REQUEST_EXCEPTION

    user = await login_service.authenticate(identifier, password)
    if not user:
        raise USER_NOT_FOUND_EXCEPTION

    return await token_creator_service.create_token_base(
        {"uid": user.id, "iac": user.is_active, "isf": user.is_staff}
    )