import bcrypt


class PasswordHashingService:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_hashed_password(password: str) -> str:
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)
        return str(password_hash)

    @staticmethod
    def verify_password(password: str, user_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), user_password.encode("utf-8"))