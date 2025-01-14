from Service.SMTPService import SMTPService
from config import settings


smtp_service = SMTPService(
    settings.MAIL_SSL, settings.MAIL_TLS, settings.MAIL_HOST,
    settings.MAIL_PORT, settings.MAIL_USER, settings.MAIL_PASSWORD
)


async def get_smtp_service():
    return smtp_service