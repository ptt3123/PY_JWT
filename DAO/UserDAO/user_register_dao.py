from sqlalchemy.future import select
from datetime import datetime, timezone

from DTO.UserDTO import UserInfoDTO
from Model import User
from Schema.UserSchema import UserRegisterSchema
from .user_dao import UserDAO


class UserRegisterDAO(UserDAO):

    """
    User DAO For Register

    Functions:

    - ``create_user``
    - ``is_username_used``
    - ``is_email_used``
    - ``is_phone_number_used``
    """

    async def create_user(self, user_register: UserRegisterSchema) \
            -> UserInfoDTO:

        """
        Create New User

        :param user_register: (:class:`UserRegisterSchema`)
        :return: (:class:`UserInfoDTO`)
        """

        user = User(**user_register.model_dump(exclude={"re_password"}))
        user.update_at = datetime.now(timezone.utc)
        user = await self.execute_with_add(user)
        return UserInfoDTO(user.username, user.first_name, user.last_name)

    async def check_user_unique_info(self, username: str, email: str, phone_number: str):

        """
        Query User Has Info Of New User

        :param username: (:class:`str`)
        :param email: (:class:`str`)
        :param phone_number: (:class:`str`)
        :return: (:class:`Tuple`) All User Have Info Like New User's Info
        """

        query = (select(User.username, User.email, User.phone_number)
                 .where((User.username.__eq__(username)) |
                        (User.email.__eq__(email)) |
                        (User.phone_number.__eq__(phone_number))))

        result = await self.execute_with_select(query)
        return result.fetchall()