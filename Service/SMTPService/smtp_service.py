import smtplib


class SMTPService:
    """"""

    def __init__(self, mail_ssl: bool, mail_tls: bool, mail_host: str,
                 mail_port: int, mail_user: str, mail_password: str):

        self.__mail_ssl = mail_ssl
        self.__mail_tls = mail_tls
        self.__mail_host = mail_host
        self.__mail_port = mail_port
        self.__mail_user = mail_user
        self.__mail_password = mail_password

    def connect(self):

        try:
            if self.__mail_ssl:
                server = smtplib.SMTP_SSL(self.__mail_host, self.__mail_port)
            else:
                server = smtplib.SMTP(self.__mail_host, self.__mail_port)
                if self.__mail_tls:
                    server.starttls()

            # Log in to the SMTP server
            server.login(self.__mail_user, self.__mail_password)
            return server

        except Exception as e:
            print(f"Error connecting to SMTP server: {e}")
            return None