from pydantic import BaseModel, EmailStr, field_validator, ValidationInfo
import re


class UserRegisterSchema(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    re_password: str

    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, first_name):
        if not isinstance(first_name, str):
            raise ValueError("first_name must be a string")

        return first_name

    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, last_name):
        if not isinstance(last_name, str):
            raise ValueError("last_name must be a string")

        return last_name

    @field_validator("username")
    @classmethod
    def validate_username(cls, username):
        if not isinstance(username, str):
            raise ValueError("username must be a string")

        return username

    @field_validator("password")
    @classmethod
    def validate_password(cls, password):
        if not isinstance(password, str):
            raise ValueError("password must be a string")

        if len(password) < 8:
            raise ValueError("password must have length greater than 8")

        if not re.search(r"[A-Z]", password):
            raise ValueError("password need at least uppercase hoa")

        if not re.search(r"[a-z]", password):
            raise ValueError("password need at least one lowercase char")

        if not re.search(r"[0-9]", password):
            raise ValueError("password need at least one digit")

        if not re.search(r"[!@#$%^&*()_+=-]", password):
            raise ValueError("password need at least 1 special char")

        return password

    @field_validator("email")
    @classmethod
    def validate_email(cls, email):
        if not isinstance(email, str):
            raise ValueError("email must be a string")

        return email

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, phone_number):
        length = 10
        if len(phone_number) != length:
            raise ValueError("Phone number must be 10 digits")

        if not phone_number.isdigit():
            raise ValueError("Phone number must contain digit only")

        return phone_number

    @field_validator("re_password")
    @classmethod
    def validate_re_password(cls, re_password, info: ValidationInfo):
        if not isinstance(re_password, str):
            raise ValueError("re_password must be a string")

        if re_password != info.data.get("password"):
            raise ValueError("re_password must same password")

        return re_password