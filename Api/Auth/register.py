from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from Dependency.ServiceDependency import get_register_service
from Schema.UserSchema import UserRegisterSchema
from Service.UserService.UserRegisterService import UserRegisterService


register_router = APIRouter()


@register_router.post("/register")
async def register(
        user: UserRegisterSchema,
        user_register_service: UserRegisterService = Depends(get_register_service)):
    """"""

    try:
        await user_register_service.register(user)
        return {"message": "success!"}

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )