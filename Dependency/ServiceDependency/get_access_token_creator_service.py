import rsa
import os

from config import settings
from Service.JWTService import AccessTokenCreatorService


public_key_path = os.path.join("Key", "public_key.pem")
with open(public_key_path, "rb") as public_key_file:
    public_key_data = public_key_file.read()
    public_key = rsa.PublicKey.load_pkcs1(public_key_data)

private_key_path = os.path.join("Key", "private_key.pem")
with open(private_key_path, "rb") as private_key_file:
    private_key_data = private_key_file.read()
    private_key = rsa.PrivateKey.load_pkcs1(private_key_data)


access_token_creator_service = AccessTokenCreatorService(
    settings.JWT_ALGORITHM, settings.ACCESS_TOKEN_EXPIRES_MINUTES,
    public_key.save_pkcs1(format="PEM"), private_key.save_pkcs1(format="PEM")
)


async def get_access_token_creator_service():
    return access_token_creator_service