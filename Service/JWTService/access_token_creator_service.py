from datetime import datetime, timezone, timedelta
import jwt

from DTO import TokenBaseDTO
from .jwt_service import JWTService


class AccessTokenCreatorService(JWTService):
    """"""
    async def create_token_base(self, data: dict) -> TokenBaseDTO:
        exp = (datetime.now(timezone.utc) +
               timedelta(minutes=self._access_token_expire_minutes))

        data.update({"exp" : exp})
        jwt_token = jwt.encode(data, self._private_key, self._algorithm)
        return TokenBaseDTO(access_token=jwt_token)