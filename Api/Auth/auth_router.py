# api end point here
from fastapi import APIRouter

from .login import login_router


auth_router = APIRouter(prefix="/Auth", tags=["Auth"])

auth_router.include_router(login_router)