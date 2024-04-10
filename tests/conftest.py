import httpx
import pytest
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.config import get_app_settings
from app.db import Base
from app.db.base import get_db
from app.db.schemas.users import UserCreate
from app.main import app
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL_TEST = "postgresql+asyncpg://postgres:admin@localhost:5432/FastAPIdb"
settings = get_app_settings()
settings.database_url = DATABASE_URL_TEST


@pytest.fixture(scope="session")
async def client():
    """Создание асинхронного клиента"""
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


DATABASE_URL_TEST = str(settings.database_url) + "_test"

async_engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_test = async_sessionmaker(
    async_engine_test, expire_on_commit=False, class_=AsyncSession
)

Base.metadata.bind = async_engine_test


async def override_get_db():
    async with async_session_test() as session:
        yield session


user = UserCreate(
    email="user5454@example.com",
    username="test",
    password="aaa",
    is_active=True,
    is_verified=True,
    is_superuser=False,
)

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True, scope="session")
async def prepare_db():
    """Создание таблиц и удаление после тестов"""
    async with async_engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with async_engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


from app.api.services.auth import current_active_user

app.dependency_overrides[current_active_user] = lambda: user
