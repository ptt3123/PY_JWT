from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from Dependency.ServiceDependency import get_register_service
from Schema.UserSchema import UserRegisterSchema
from Service.UserService.UserRegisterService import UserRegisterService
from exception import DATABASE_EXCEPTION


register_router = APIRouter()


@register_router.post("/register")
async def register(
        user: UserRegisterSchema,
        user_register_service: UserRegisterService = Depends(get_register_service)):

    """
    Endpoint For User To Register

    :param user: (:class:`UserRegisterSchema`) Info Of User

    :param user_register_service: (:class:`UserRegisterService`) Service To Register User

    :return: (:class:`UserInfoDTO`)
    """

    try:
        new_user = await user_register_service.register(user)
        return new_user

    except IntegrityError as exception:

        exception_dict = await user_register_service.check_unique(
            user.username, user.email, user.phone_number)

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=exception_dict,
        )

    except SQLAlchemyError as e:
        print(str(e))
        raise DATABASE_EXCEPTION