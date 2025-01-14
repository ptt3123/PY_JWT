from datetime import datetime, timezone, timedelta
import jwt, asyncio

from DTO import TokenBaseDTO
from .jwt_service import JWTService


class AccessTokenCreatorService(JWTService):
    """"""
    async def create_token_base(self, data: dict) -> TokenBaseDTO:
        exp = (datetime.now(timezone.utc) +
               timedelta(minutes=self._access_token_expire_minutes))

        data.update({"exp" : exp})
        key = self._private_key
        algorithm = self._algorithm
        jwt_token = await asyncio.to_thread(jwt.encode, data, key, algorithm)
        return TokenBaseDTO(access_token=jwt_token)