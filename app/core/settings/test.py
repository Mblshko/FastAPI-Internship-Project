from pydantic import PostgresDsn, SecretStr

from app.core.settings.app_settings import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test FastAPI example application"

    secret_key: SecretStr = SecretStr("test")

    database_url: PostgresDsn
