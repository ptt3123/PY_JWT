from DTO.UserDTO import UserInfoDTO
from Schema.UserSchema import UserRegisterSchema
from ..user_service import UserService
from DAO.UserDAO import UserRegisterDAO


class UserRegisterService(UserService):
    """"""

    def __init__(self, user_register_dao: UserRegisterDAO):
        self._user_register_dao = user_register_dao

    async def register(self, user_register: UserRegisterSchema) -> UserInfoDTO:
        return await self._user_register_dao.create_user(user_register)