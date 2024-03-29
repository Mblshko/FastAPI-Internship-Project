from fastapi import FastAPI, Depends

from app.api.routers.articles import router as articles_router
from app.api.routers.comments import router as comments_router
from app.api.routers.profile import router as profile_router
from app.api.services.auth import auth_backend, fastapi_users, current_active_user
from app.core.middelware import TestMiddelware
from app.db import User
from app.db.schemas.users import UserRead, UserCreate


app = FastAPI()
app.include_router(
    router=articles_router,
    prefix="/articles",
    tags=["Articles"],
)

app.include_router(router=comments_router, prefix="/comments", tags=["Comments"])
app.include_router(router=profile_router, prefix="/profile", tags=["Profile"])

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.username}!"}


check_active_user = TestMiddelware()
app.middleware("http")(check_active_user)
