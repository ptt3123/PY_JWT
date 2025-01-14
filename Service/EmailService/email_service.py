import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTP_SSL

from config import settings


class EmailService:

    @staticmethod
    def send_mail(server: SMTP | SMTP_SSL,
                  email_to: str, subject: str = "",
                  html_content: str = "")\
            -> None:

        msg = MIMEMultipart()
        msg["From"] = settings.EMAILS_FROM_EMAIL
        msg["To"] = email_to
        msg["Subject"] = subject

        msg.attach(MIMEText(html_content, "html"))

        try:
            server.send_message(msg)
        except Exception as e:
            print(f"Error sending email: {e}")
        finally:
            server.quit()