from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from Service.JWTService import AccessTokenValidatorService
from ..ServiceDependency import get_access_token_validator_service


oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "auth/login")


async def validate_jwt(
        token: str = Depends(oauth2_scheme),
        validator_service: AccessTokenValidatorService = Depends(get_access_token_validator_service)
):

    return await validator_service.validate_token(token)