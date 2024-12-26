import rsa
import os
from abc import ABC


class JWTService(ABC):
    """"""
    def __init__(self):
        self._algorithm = "RS256"
        self._access_token_expire_minutes = 15

        # Read Key
        public_key_path = os.path.join("Key", "public_key.pem")
        with open(public_key_path, "rb") as public_key_file:
            public_key_data = public_key_file.read()
            public_key = rsa.PublicKey.load_pkcs1(public_key_data)
            self._public_key = public_key.save_pkcs1(format="PEM")

        private_key_path = os.path.join("Key", "private_key.pem")
        with open(private_key_path, "rb") as private_key_file:
            private_key_data = private_key_file.read()
            private_key = rsa.PrivateKey.load_pkcs1(private_key_data)
            self._private_key = private_key.save_pkcs1(format="PEM")