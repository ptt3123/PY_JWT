from datetime import datetime, timezone, timedelta
import jwt

from Schema import TokenBase
from .jwt_service import JWTService


class AccessTokenCreatorService(JWTService):
    """"""
    async def create_token_base(self, data: dict) -> TokenBase:
        exp = (datetime.now(timezone.utc) +
               timedelta(minutes=self._access_token_expire_minutes))

        data.update({"exp" : exp})
        jwt_token = jwt.encode(data, self._private_key, self._algorithm)
        return TokenBase(access_token=jwt_token)