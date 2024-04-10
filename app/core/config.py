from app.core.settings.app_settings import AppSettings
from app.core.settings.base import AppEnvTypes, BaseAppSettings
from app.core.settings.test import TestAppSettings

environments: dict[AppEnvTypes, type[AppSettings]] = {
    AppEnvTypes.dev: AppSettings,
    AppEnvTypes.test: TestAppSettings,
}


def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()


settings = get_app_settings()
