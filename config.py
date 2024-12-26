from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str
    DATABASE_URL: str
    MAX_LOGIN_PER_IP: int
    MINUTES_LOCK_LOGIN_PER_IP: int

    model_config= SettingsConfigDict(extra= "ignore", env_file= ".env")


settings= Settings()