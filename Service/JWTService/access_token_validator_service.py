import jwt

from DTO import TokenDataDTO
from exception import EXPIRED_TOKEN, INVALID_TOKEN
from .jwt_service import JWTService


class AccessTokenValidatorService:
    """"""
    def __init__(self, jwt_service: JWTService):
        self._jwt_service = jwt_service

    async def validate_token(self, token: str) -> TokenDataDTO:
        try:
            dic: dict = jwt.decode(
                token, self._jwt_service.public_key, self._jwt_service.algorithm,
                options={"verify_exp": True}
            )
            dic.pop("exp")
            return TokenDataDTO(**dic)


        except jwt.ExpiredSignatureError:
            raise EXPIRED_TOKEN

        except jwt.InvalidTokenError:
            raise INVALID_TOKEN