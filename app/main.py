from fastapi import FastAPI, Depends

from app.api.routers.base import base_router
from app.api.services.auth import current_active_user
from app.core.config import settings
from app.core.middelware import TestMiddelware
from app.db import User
from app.core.settings.app_settings import AppSettings


def setup_middleware(application: FastAPI) -> None:
    middleware = TestMiddelware()
    application.middleware("http")(middleware)


def setup_routers(application: FastAPI) -> None:
    application.include_router(base_router)


def get_application(setting: AppSettings) -> FastAPI:
    data = setting.fastapi_kwargs()
    application = FastAPI(**data)

    setup_routers(application)
    setup_middleware(application)
    return application


app = get_application(settings)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.username}!"}
