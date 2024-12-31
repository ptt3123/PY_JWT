from datetime import datetime, timezone

from DTO.UserDTO import UserInfoDTO
from Model import User
from Schema.UserSchema import UserRegisterSchema
from .user_dao import UserDAO


class UserRegisterDAO(UserDAO):
    """"""

    async def create_user(self, user_register: UserRegisterSchema) \
            -> bool:
        """"""

        user = User(**user_register.model_dump(exclude={"re_password"}))
        user.update_at = datetime.now(timezone.utc)
        user = await self.execute_with_add(user)
        return True