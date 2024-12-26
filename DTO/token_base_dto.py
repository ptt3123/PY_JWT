class TokenBaseDTO:
    """"""

    def __init__(self, access_token: str, token_type: str = 'bearer'):
        self.access_token = access_token
        self.token_type = token_type

    def dict(self):
        return {
            "access_token": self.access_token,
            "token_type": self.token_type
        }