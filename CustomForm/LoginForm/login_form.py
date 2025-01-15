from fastapi.security import OAuth2PasswordRequestForm

class LoginForm(OAuth2PasswordRequestForm):
    def __init__(
        self,
        grant_type: str = None,
        username: str = None,
        password: str = None,
        scope: str = "",
        client_id: str = None,
        client_secret: str = None,
        method: str = "username",
    ):

        super().__init__(
            grant_type=grant_type,
            username=username,
            password=password,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
        )
        self.method = method
