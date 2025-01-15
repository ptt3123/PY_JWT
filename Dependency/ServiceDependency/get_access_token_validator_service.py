from fastapi import Depends

from Service.JWTService import JWTService, AccessTokenValidatorService
from .get_jwt_service import get_jwt_service


async def get_access_token_validator_service(
        jwt_service: JWTService = Depends(get_jwt_service)
):

    return AccessTokenValidatorService(jwt_service)