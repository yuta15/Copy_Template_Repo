from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    """Settings for the application."""
    GITHUB_TOKEN: str = os.environ.get('GITHUB_TOKEN')
    GITHUB_ACTOR: str = os.environ.get('GITHUB_ACTOR')
    ROOT_DIR: str = os.getcwd()
    PARAMETER_FILE: str = f'{ROOT_DIR}/params.json'

    model_config = SettingsConfigDict(
        env_file='env',
        env_file_encoding='utf-8'
    )
    
setting = Settings()