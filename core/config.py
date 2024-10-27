from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
from dotenv import load_dotenv

load_dotenv()


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 4000


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="CONFIG__",
        env_file_encoding="utf-8",
    )
    run: RunConfig = RunConfig()


settings = Settings()
