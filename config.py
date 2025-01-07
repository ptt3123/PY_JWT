from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str

    DATABASE_URL: str

    MAX_REQUEST_PER_IP: int
    MINUTES_LOCK_REQUEST_PER_IP: int

    MAX_LOGIN_PER_IP: int
    MINUTES_LOCK_LOGIN_PER_IP: int

    MAX_REQUEST_PER_WINDOW: int
    MINUTES_PER_WINDOW: int

    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRES_MINUTES: int

    model_config = SettingsConfigDict(extra = "ignore", env_file = ".env")


settings= Settings()