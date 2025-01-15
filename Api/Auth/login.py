from fastapi import APIRouter, Request, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from typing import Optional

from DTO import TokenDataDTO
from Dependency.ServiceDependency import (get_login_service, get_smtp_service,
                                          get_access_token_creator_service)
from Dependency.EndpointDependency import login_limit_dependency
from Service.SMTPService import SMTPService
from exception import USER_NOT_FOUND_EXCEPTION, DATABASE_EXCEPTION
from Service.UserService import UserLoginService
from Service.JWTService import AccessTokenCreatorService
from Service.EmailService import EmailService
from Service.EmailTemplateService import EmailTemplateService


login_router = APIRouter()


@login_router.post("/login")
async def login(
        request: Request, background_tasks: BackgroundTasks,
        method: Optional[str] = "username", user_form: OAuth2PasswordRequestForm = Depends(),
        login_limit = Depends(login_limit_dependency),
        login_service: UserLoginService = Depends(get_login_service),
        token_creator_service: AccessTokenCreatorService =
        Depends(get_access_token_creator_service),
        smtp_service: SMTPService = Depends(get_smtp_service)
):

    """
    Endpoint For User To Login

    :param user_form: (:class:`UserLoginSchema`) Info Of User For Log in, Common Is ``identifier`` And ``password``

    :param background_tasks: (:class:`BackgroundTasks`)

    :param smtp_service: (:class:`SMTPService`)

    :param request: (:class:`Request`)

    :param method: (:class:`str`) Method User Want Login By. Ex "username", "email", ...

    :param login_limit: (:class:`None`) Call Dependency For Check If User Can Log in More

    :param login_service: (:class:`UserLoginService`) Service For Handle Request Log in Of User

    :param token_creator_service: (:class:`AccessTokenCreatorService`) Service For Create JWT For Authenticate

    :return: (:class:`TokenBaseDTO`)
    """

    try:
        user = await login_service.authenticate(user_form.username, user_form.password)
        if not user:
            raise USER_NOT_FOUND_EXCEPTION


        # Notify by email
        if smtp_service:
            server = smtp_service.connect()
            html_template = EmailTemplateService.get_login_notification_template(
                user.username,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

            background_tasks.add_task(
                EmailService.send_mail,
                server, user.email, "Login Notification", html_template)


        token = await token_creator_service.create_token_base(
            TokenDataDTO(user.id, user.is_active, user.is_staff)
        )


        response = JSONResponse(content=token.dict())
        response.set_cookie(
            key="refresh_token", value=token.access_token, max_age=3*3600,
            domain="127.0.0.1", path="/auth/refresh",
            httponly=True, secure=False, samesite="strict"
        )
        return response


    except SQLAlchemyError as e:
        print(str(e))
        raise DATABASE_EXCEPTION