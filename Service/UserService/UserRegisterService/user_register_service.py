from Service.PasswordHashingService import PasswordHashingService
from DTO.UserDTO import UserInfoDTO
from Schema.UserSchema import UserRegisterSchema
from ..user_service import UserService
from DAO.UserDAO import UserRegisterDAO


class UserRegisterService(UserService):
    """"""

    def __init__(self, user_register_dao: UserRegisterDAO):
        self._user_register_dao = user_register_dao

    async def register(self, user_register: UserRegisterSchema) -> UserInfoDTO:
        """
        Hashing Password Before Call :class:`UserRegisterDao` To Add User To Database

        :param user_register: :class:`UserRegisterSchema`
        :return: :class:`UserInfoDTO`
        """
        user_register.password = (
            PasswordHashingService.get_hashed_password(user_register.password))

        return await self._user_register_dao.create_user(user_register)

    async def check_unique(self, username: str, email: str, phone_number: str)\
            -> dict[str, str]:
        """
        Check If Info Of User Unique And Return A Exception Info With Form Of A Dict

        :param username: str
        :param email: str
        :param phone_number: str
        :return: Exception Dict Like {"ptt": "This Username Has Been Used!!!"}, ...
        """

        users = await self._user_register_dao.check_user_unique_info(
            username, email, phone_number
        )

        exception_dict = {}

        for user in users:
            if user.username == username:
                exception_dict["username"] = "This Username Has Been Used!!!"
            if user.email == email:
                exception_dict["email"] = "This Email Has Been Used!!!"
            if user.phone_number == phone_number:
                exception_dict["phone_number"] = "This Phone Number Has Been Used!!!"

        return exception_dict