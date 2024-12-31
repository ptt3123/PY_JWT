from fastapi import APIRouter, Request, Depends, Body, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from Schema.UserSchema import UserLoginSchema
from Dependency.ServiceDependency import get_login_service
from Dependency.EndpointDependency import login_limit_dependency
from exception import USER_NOT_FOUND_EXCEPTION
from Service.JWTService import AccessTokenCreatorService


login_router = APIRouter()


@login_router.post("/login")
async def login(request: Request, method: str, user: UserLoginSchema = Body(),
                login_limit = Depends(login_limit_dependency),
                login_service = Depends(get_login_service),
                token_creator_service: AccessTokenCreatorService = Depends()):
    """ Return TokenBaseDTO """

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