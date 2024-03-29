from sqlalchemy.ext.asyncio import AsyncSession

from app.db import User, Profile
from app.db.schemas.profile import ProfileCreate


class ProfileService:
    @staticmethod
    async def create_profile(
        session: AsyncSession,
        profile_data: ProfileCreate,
        user: User,
    ) -> Profile:
        data = profile_data.model_dump()
        data["user_id"] = user.id
        profile = Profile(**data)
        session.add(profile)
        await session.commit()
        return profile
