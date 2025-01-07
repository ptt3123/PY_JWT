from fastapi import APIRouter, Request, Depends, Body, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from Schema.UserSchema import UserLoginSchema
from Dependency.ServiceDependency import (get_login_service,
                                          get_access_token_creator_service)
from Dependency.EndpointDependency import login_limit_dependency
from exception import USER_NOT_FOUND_EXCEPTION
from Service.UserService import UserLoginService
from Service.JWTService import AccessTokenCreatorService


login_router = APIRouter()


@login_router.post("/login")
async def login(request: Request, method: str, user: UserLoginSchema = Body(),
                login_limit = Depends(login_limit_dependency),
                login_service: UserLoginService = Depends(get_login_service),
                token_creator_service: AccessTokenCreatorService =
                Depends(get_access_token_creator_service)):

    """
    Endpoint For User To Login

    :param request: (:class:`Request`)
    :param method: (:class:`str`) Method User Want Login By. Ex "username", "email", ...
    :param user: (:class:`UserLoginSchema`) Info Of User For Log in, Common Is ``identifier`` And ``password``
    :param login_limit: (:class:`None`) Call Dependency For Check If User Can Log in More
    :param login_service: (:class:`UserLoginService`) Service For Handle Request Log in Of User
    :param token_creator_service: (:class:`AccessTokenCreatorService`) Service For Create JWT For Authenticate
    :return: (:class:`TokenBaseDTO`)
    """

    try:
        user = await login_service.authenticate(user.identifier, user.password)
        if not user:
            raise USER_NOT_FOUND_EXCEPTION

        return await token_creator_service.create_token_base(
            {"uid": user.id, "iac": user.is_active, "isf": user.is_staff}
        )

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )