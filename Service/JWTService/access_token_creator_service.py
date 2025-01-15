from datetime import datetime, timezone, timedelta
import jwt

from DTO import TokenBaseDTO, TokenDataDTO
from .jwt_service import JWTService


class AccessTokenCreatorService:
    """"""
    def __init__(self, jwt_service: JWTService):
        self._jwt_service = jwt_service

    async def create_token_base(self, data: TokenDataDTO) -> TokenBaseDTO:
        exp = (datetime.now(timezone.utc) +
               timedelta(minutes=self._jwt_service.access_token_expire_minutes))

        dic = data.dict()
        dic.update({"exp" : exp})

        jwt_token = jwt.encode(
            dic,
            self._jwt_service.private_key,
            self._jwt_service.algorithm
        )
        return TokenBaseDTO(access_token=jwt_token)