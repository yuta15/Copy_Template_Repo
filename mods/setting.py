from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    """Settings for the application."""
    PERSONAL_TOKEN: str = os.environ.get('PERSONAL_TOKEN')
    GITHUB_ACTOR: str = os.environ.get('GITHUB_ACTOR')
    ROOT_DIR: str = os.getcwd()
    PARAMETER_FILE: str = f'{ROOT_DIR}/params.json'
    USERNAME: str = "yuta15"

    model_config = SettingsConfigDict(
        env_file='env',
        env_file_encoding='utf-8'
    )
    
setting = Settings()