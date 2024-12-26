from DAO.UserDAO import UserLoginDAO
from .user_login_service import UserLoginService
from .user_login_by_username_service import UserLoginByUsernameService
from .user_login_by_email_service import UserLoginByEmailService


class UserLoginServiceFactory:

    @staticmethod
    def get_user_login_service(method: str, user_login_dao: UserLoginDAO) \
            -> UserLoginService:

        """"""
        if method == "username":
            return UserLoginByUsernameService(user_login_dao)

        elif method == "email":
            return UserLoginByEmailService(user_login_dao)

        else:
            raise Exception("Method Not Found!!!")