from Service.PasswordHashingService import PasswordHashingService
from DTO.UserDTO import UserInfoDTO
from Schema.UserSchema import UserRegisterSchema
from ..user_service import UserService
from DAO.UserDAO import UserRegisterDAO


class UserRegisterService(UserService):
    """"""

    def __init__(self, user_register_dao: UserRegisterDAO):
        self._user_register_dao = user_register_dao

    async def register(self, user_register: UserRegisterSchema) -> bool:

        user_register.password = (
            PasswordHashingService.get_hashed_password(user_register.password))

        return await self._user_register_dao.create_user(user_register)