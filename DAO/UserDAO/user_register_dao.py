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

    async def is_username_used(self, username: str) -> bool:
        """
        If Username Has Been Used Return True, Else False

        :param username: (:class:`str`)
        :return: (:class:`bool`)
        """

        query = select(User.username).where(User.username.__eq__(username))
        result = await self.execute_with_select(query)

        if result.scalar():
            return True
        else:
            return False

    async def is_email_used(self, email: str) -> bool:
        """
        If Email Has Been Used Return True, Else False

        :param email: (:class:`str`)
        :return: (:class:`bool`)
        """

        query = select(User.username).where(User.email.__eq__(email))
        result = await self.execute_with_select(query)

        if result.scalar():
            return True
        else:
            return False

    async def is_phone_number_used(self, phone_number: str) -> bool:
        """
        If Phone Number Has Been Used Return True, Else False

        :param phone_number: (:class:`str`)
        :return: (:class:`bool`)
        """

        query = select(User.username).where(User.phone_number.__eq__(phone_number))
        result = await self.execute_with_select(query)

        if result.scalar():
            return True
        else:
            return False