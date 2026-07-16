from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.dev",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    apikey: str = ""
    yt_dlp_timeout: int = 15
    yt_dlp_player_client: str = "android"
    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = True


settings = Settings()
