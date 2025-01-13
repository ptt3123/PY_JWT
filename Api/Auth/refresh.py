from fastapi import APIRouter, Request

from exception import REFRESH_TOKEN_NOT_FOUND
from DTO import TokenBaseDTO


refresh_router = APIRouter()


@refresh_router.get("/refresh")
async def refresh(request: Request):
    """
    Use Refresh Token In Cookie To Return New Access Token. If Refresh Token Not Found Raise Exception

    :param request: (:class:`Request`)
    :return:
    """

    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise REFRESH_TOKEN_NOT_FOUND

    return TokenBaseDTO(access_token=refresh_token)