from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.schemas.articles import Article, ArticleCreate
from app.db.base import get_db
from app.api.services.articles import ArticlesCRUD


router = APIRouter(tags=["Articles"], prefix="/articles")


@router.get("", response_model=list[Article])
async def get_articles(session: AsyncSession = Depends(get_db)):
    return await ArticlesCRUD.list_article(session=session)


@router.get("/{article_id}", response_model=Article)
async def get_article(article_id: int, session: AsyncSession = Depends(get_db)):
    return await ArticlesCRUD.detail_article(session=session, article_id=article_id)


@router.post("", response_model=Article)
async def create_article(
        article_data: Annotated[ArticleCreate, Depends()],
        session: AsyncSession = Depends(get_db)
):
    return await ArticlesCRUD.create_article(session=session, article_data=article_data)


@router.delete("/{article_id}")
async def delete_article(article_id: int, session: AsyncSession = Depends(get_db)):
    return await ArticlesCRUD.delete_article(article_id=article_id, session=session)
