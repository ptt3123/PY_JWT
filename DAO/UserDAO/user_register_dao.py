from .user_dao import UserDAO


class UserRegisterDAO(UserDAO):
    """"""

    async def create_user(self, user: dict):
        async with self._session_maker() as session:
            pass
