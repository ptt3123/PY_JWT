# api end point here
from fastapi import APIRouter

from .login import login_router
from .register import register_router
from .refresh import refresh_router
from .get_csrf_token import get_csrf_token_router
from .info import info_router


auth_router = APIRouter(prefix="/auth", tags=["auth"])

auth_router.include_router(login_router)
auth_router.include_router(register_router)
auth_router.include_router(refresh_router)
auth_router.include_router(get_csrf_token_router)
auth_router.include_router(info_router)