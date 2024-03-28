from fastapi import FastAPI

from app.api.routers.articles import router as articles_router
from app.api.services.auth import auth_backend, fastapi_users
from app.db.schemas.users import UserRead, UserCreate


app = FastAPI()
app.include_router(
    router=articles_router,
    prefix="/articles",
    tags=["articles"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
