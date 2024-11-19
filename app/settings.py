from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = 'DataBase API'
    app_host: str = '0.0.0.0'
    app_port: int = 3000

    database_url: str = "postgresql+psycopg://stanuser:pgpwd4stan@192.168.1.66:6432/standb"

    project_root: Path = Path(__file__).parent.parent.resolve()

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()