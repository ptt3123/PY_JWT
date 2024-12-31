from pydantic import BaseModel


class UserLoginSchema(BaseModel):

    """
    Schema Of User For Login

    Properties:

    - ``identifier`` (str): Maybe Username Or Email
    - ``password`` (str): Password Of User

    """
    identifier: str
    password: str