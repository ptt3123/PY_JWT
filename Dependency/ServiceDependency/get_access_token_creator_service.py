from fastapi import Depends

from Service.JWTService import JWTService, AccessTokenCreatorService
from .get_jwt_service import get_jwt_service


async def get_access_token_creator_service(
        jwt_service: JWTService = Depends(get_jwt_service)
):

    return AccessTokenCreatorService(jwt_service)