from datetime import datetime, timezone, timedelta
from itsdangerous import URLSafeTimedSerializer, BadSignature


class CRSFTokenService:

    _serializer: URLSafeTimedSerializer

    def __init__(self, secret_key: str):
        self._serializer = URLSafeTimedSerializer(secret_key)

    async def generate_csrf_token(self, minutes: int = 1):
        exp = ((datetime.now(timezone.utc) + timedelta(minutes=minutes))
               .isoformat())
        token_data = {"exp": exp}
        return self._serializer.dumps(token_data)

    async def verify_csrf_token(self, csrf_token: str):
        try:
            token_data = self._serializer.loads(csrf_token)
            exp = datetime.fromisoformat(token_data.get("exp"))

            if datetime.now(timezone.utc) > exp:
                return False

            return True
        except BadSignature:
            return False