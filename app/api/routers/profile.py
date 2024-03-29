from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services.auth import current_active_user
from app.api.services.profile import ProfileService
from app.db import User
from app.db.base import get_db
from app.db.schemas.profile import ProfileCreate, Profile

router = APIRouter()


@router.post("", response_model=Profile, status_code=201)
async def create_profile(
    profile_data: Annotated[ProfileCreate, Depends()],
    session: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await ProfileService.create_profile(
        session=session, profile_data=profile_data, user=user
    )
