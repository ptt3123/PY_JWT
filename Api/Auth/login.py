from fastapi import APIRouter, Request, Depends, Form, BackgroundTasks, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

from Schema.UserSchema import UserLoginSchema
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
        method: str, user: UserLoginSchema = Form(),
        login_limit = Depends(login_limit_dependency),
        login_service: UserLoginService = Depends(get_login_service),
        token_creator_service: AccessTokenCreatorService =
        Depends(get_access_token_creator_service),
        smtp_service: SMTPService = Depends(get_smtp_service)
):

    """
    Endpoint For User To Login

    :param background_tasks: (:class:`BackgroundTasks`)
    :param smtp_service: (:class:`SMTPService`)
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
            {"uid": user.id, "iac": user.is_active, "isf": user.is_staff}
        )


        response = JSONResponse(content=token.dict())
        response.set_cookie(
            key="refresh_token", value=token.access_token,
            domain="127.0.0.1", max_age=3*3600,
            path="/auth/refresh", httponly=True, secure=False
        )
        return response


    except SQLAlchemyError as e:
        print(str(e))
        raise DATABASE_EXCEPTION