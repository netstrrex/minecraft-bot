from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class BotSettings(BaseModel):
    token: str = ""


class MinecraftServerSettings(BaseModel):
    ip: str = "127.0.0.1"
    rcon_port: int = 25575
    rcon_password: str = "1111"


class Settings(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__",
    )
    bot: BotSettings = BotSettings()
    minecraft_server: MinecraftServerSettings = MinecraftServerSettings()


settings = Settings()
