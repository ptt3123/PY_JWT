from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from Dependency.ServiceDependency import get_csrf_token_service
from Service.CSRFTokenService import CRSFTokenService


get_csrf_token_router = APIRouter()


@get_csrf_token_router.get("/get_csrf_token")
async def get_csrf_token(
        csrf_token_service: CRSFTokenService = Depends(get_csrf_token_service)
):

    token = await csrf_token_service.generate_csrf_token()

    response = JSONResponse({"message": "OK"})
    response.set_cookie(
        key="csrf_token", value=token,
        domain="127.0.0.1", httponly=True, secure=False
    )
    return response
