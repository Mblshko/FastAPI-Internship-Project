from pydantic import PostgresDsn, SecretStr

from app.core.config import BaseAppSettings


class AppSettings(BaseAppSettings):
    debug: bool = True
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI example application"
    version: str = "0.0.0"

    database_url: PostgresDsn

    secret_key: SecretStr

    api_prefix: str = "/api"

    allowed_hosts: list[str] = ["*"]


settings = AppSettings()
