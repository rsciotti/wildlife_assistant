from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Model settings
    MODEL_NAME: str = "claude-3-5-haiku-latest"
    ANTHROPIC_API_KEY: str
    LOGFIRE_TOKEN: str

    # MCP settings
    LOCATION_MCP_URL: str = 'https://demo-endpoints.pydantic.workers.dev/latlng'
    WEATHER_MCP_URL: str = 'https://demo-endpoints.pydantic.workers.dev/'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    return Settings()