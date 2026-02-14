from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import Field

class Settings(BaseSettings):
    # App Settings
    PROJECT_NAME: str = "Life OS"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Database Settings
    DATABASE_URL: str = Field(default="postgresql+psycopg2://postgres:postgres@localhost:5432/life_os")
    
    # Redis Settings
    REDIS_URL: str = Field(default="redis://localhost:6379/0")
    
    # CORS Settings
    CORS_ORIGINS: List[str] = ["*"]
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )

settings = Settings()
