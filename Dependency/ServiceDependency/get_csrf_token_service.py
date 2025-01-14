from Service.CSRFTokenService import CRSFTokenService
from config import settings


csrf_token_service = CRSFTokenService(settings.SECRET_KEY)

async def get_csrf_token_service():
    return csrf_token_service