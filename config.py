from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str

    DATABASE_URL: str

    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRES_MINUTES: int

    MAX_REQUEST_PER_WINDOW: int
    SECONDS_PER_WINDOW: int

    MAX_LOGIN_REQUEST_PER_WINDOW_BY_IP: int
    SECONDS_PER_WINDOW_FOR_LOGIN_REQUEST_BY_IP: int

    MAX_LOGIN_REQUEST_PER_WINDOW_BY_IDENTIFIER: int
    SECONDS_PER_WINDOW_FOR_LOGIN_REQUEST_BY_IDENTIFIER: int

    MAIL_TLS: bool = True
    MAIL_SSL: bool = False
    MAIL_HOST: str
    MAIL_PORT: int = 587
    MAIL_USER: str
    MAIL_PASSWORD: str
    EMAILS_FROM_EMAIL: str | None = None

    model_config = SettingsConfigDict(extra = "ignore", env_file = ".env")


settings = Settings()