from typing import Sequence

from fastapi import HTTPException

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.models.articles import Article, Comment
from app.db.models.users import User
from app.db.schemas.articles import ArticleCreate


class ArticlesCRUD:
    @staticmethod
    async def list_article(session: AsyncSession) -> Sequence[Article]:
        stmt = select(Article).order_by(Article.created)
        result = await session.execute(stmt)
        articles = result.scalars().all()
        return articles

    @staticmethod
    async def detail_article(session: AsyncSession, article_id: int) -> Article | None:
        try:
            stmt = (
                select(Article, Comment)
                .join(Article.comments)
                .where(Article.id == article_id)
            )
            result = await session.execute(stmt)
            res = result.scalar()
            return res
        except:
            raise HTTPException(status_code=404, detail="Article not found")

    @staticmethod
    async def create_article(
        session: AsyncSession,
        article_data: ArticleCreate,
        user: User,
    ) -> Article:
        data = article_data.model_dump()
        data["user_id"] = user.id
        article = Article(**data)
        session.add(article)
        await session.commit()
        return article

    @staticmethod
    async def delete_article(session: AsyncSession, article_id: int) -> None:
        stmt = delete(Article).where(Article.id == article_id)
        await session.execute(stmt)
        await session.commit()

    @staticmethod
    async def update_article(
        session: AsyncSession, article_data: ArticleCreate, article_id: int
    ) -> None:
        try:
            stmt = (
                update(Article)
                .where(Article.id == article_id)
                .values(**article_data.model_dump())
            )
            await session.execute(stmt)
            await session.commit()
        except:
            raise HTTPException(status_code=404, detail="Article not found")
