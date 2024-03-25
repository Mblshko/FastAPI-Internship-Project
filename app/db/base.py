from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.settings.app_settings import AppSettings, settings

Base = declarative_base()

async_engine = create_async_engine(settings.database_url.unicode_string(), echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_db():
    async with async_session() as session:
        yield session
