from fastapi import FastAPI, Request

from exception import (USER_NOT_FOUND_EXCEPTION,
                       METHOD_NOT_FOUND_EXCEPTION,
                       TOO_MUCH_LOGIN_REQUEST_EXCEPTION)
from Service.LoginLimitService import LoginLimitPerIPService
from DAO.UserDAO import UserLoginDAO
from Service.UserService.UserLoginService import UserLoginServiceFactory
from Service.JWTService import AccessTokenCreatorService


app = FastAPI()


@app.post("/login")
async def login(request: Request, identifier: str, password: str, method: str):
    """"""

    login_limit_service = LoginLimitPerIPService()
    if not await login_limit_service.check(request.client.host):
        raise TOO_MUCH_LOGIN_REQUEST_EXCEPTION

    user_login_dao = UserLoginDAO()
    try:
        service = UserLoginServiceFactory.get_user_login_service(
            method, user_login_dao)

    except Exception as e:
        raise METHOD_NOT_FOUND_EXCEPTION

    user = await service.authenticate(identifier, password)
    if not user:
        raise USER_NOT_FOUND_EXCEPTION

    token_creator_service = AccessTokenCreatorService()
    return await token_creator_service.create_token_base(
        {"uid": user.id, "iac": user.is_active, "isf": user.is_staff}
    )