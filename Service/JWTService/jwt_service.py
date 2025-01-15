from abc import ABC


class JWTService(ABC):
    """"""
    def __init__(self, algorithm: str, access_token_expire_minutes: int,
                 public_key: bytes, private_key: bytes):

        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes
        self.public_key = public_key
        self.private_key = private_key