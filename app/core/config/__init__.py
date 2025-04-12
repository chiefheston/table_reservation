__all__ = [
    "settings",
]

from pydantic_settings import BaseSettings

from dotenv import load_dotenv

from .app import AppConfig
from .db import DBConfig

load_dotenv()


class Settings(
    AppConfig,
    DBConfig,
    BaseSettings,
):
    class Config:
        env_file = ".env"


settings = Settings()
