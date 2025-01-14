from abc import ABC


class JWTService(ABC):
    """"""
    def __init__(self, algorithm: str, access_token_expire_minutes: int,
                 public_key: bytes, private_key: bytes):

        self._algorithm = algorithm
        self._access_token_expire_minutes = access_token_expire_minutes
        self._public_key = public_key
        self._private_key = private_key