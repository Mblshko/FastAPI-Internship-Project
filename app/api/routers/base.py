from fastapi import APIRouter
from app.api.routers.articles import router as articles_router
from app.api.routers.profile import router as profile_router
from app.api.routers.comments import router as comments_router
from app.api.services.auth import auth_backend, fastapi_users
from app.db.schemas.users import UserRead, UserCreate

base_router = APIRouter()
base_router.include_router(
    router=articles_router,
    prefix="/articles",
    tags=["Articles"],
)

base_router.include_router(
    router=comments_router, prefix="/comments", tags=["Comments"]
)
base_router.include_router(router=profile_router, prefix="/profile", tags=["Profile"])

base_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

base_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
