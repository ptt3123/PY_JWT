from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone

from DTO.UserDTO import UserInfoDTO
from Model import User
from Schema.UserSchema import UserRegisterSchema
from .user_dao import UserDAO


class UserRegisterDAO(UserDAO):
    """"""

    async def create_user(self, user_register: UserRegisterSchema) \
            -> UserInfoDTO:
        """"""

        user = User(**user_register.model_dump(exclude={"re_password"}))
        user.update_at = datetime.now(timezone.utc)

        try:
            async with self._session_maker() as session:
                session.add(user)
                await session.commit()
                await session.refresh(user)

        except SQLAlchemyError as e:
            await session.rollback()
            raise Exception(str(e))

        return UserInfoDTO(user.username, user.first_name, user.last_name)