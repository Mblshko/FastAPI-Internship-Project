from fastapi import HTTPException, Depends

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services.auth import current_active_user
from app.db.models.articles import Article, Comment
from app.db.models.users import get_user_db, User
from app.db.schemas.articles import ArticleCreate


class ArticlesCRUD:
    @classmethod
    async def list_article(cls, session: AsyncSession) -> list[Article]:
        stmt = select(Article).order_by(Article.created)
        result = await session.execute(stmt)
        articles = result.scalars().all()
        return articles

    @classmethod
    async def detail_article(cls, session: AsyncSession, article_id: int) -> Article | None:
        try:
            stmt = select(Article).filter_by(id=article_id)
            result = await session.execute(stmt)
            return result.scalar_one()
        except:
            raise HTTPException(status_code=404, detail="Article not found")

    @classmethod
    async def create_article(cls, session: AsyncSession,
                             article_data: ArticleCreate,
                             user: User = Depends(current_active_user)
                             ) -> Article:
        data = article_data.model_dump()
        data['user_id'] = user.id
        article = Article(data)
        session.add(article)
        await session.commit()
        return article

    @classmethod
    async def delete_article(cls, session: AsyncSession, article_id: int) -> None:
        stmt = delete(Article).filter_by(id=article_id)
        await session.execute(stmt)
        await session.commit()


    @classmethod
    async def update_article(cls, session: AsyncSession, article_data: ArticleCreate) -> Article:
        article = Article(**article_data.model_dump())

