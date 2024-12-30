from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    identifier: str
    password: str