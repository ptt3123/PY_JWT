# api end point here
from fastapi import APIRouter

from .Auth import auth_router


router = APIRouter()

router.include_router(auth_router)