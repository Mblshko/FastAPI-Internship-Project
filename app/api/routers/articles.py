from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services.auth import current_active_user
from app.api.services.comments import CommentsService
from app.db import User
from app.db.schemas.articles import Article, ArticleCreate, ArticleDetail
from app.db.schemas.comments import Comment, CommentCreate
from app.db.base import get_db
from app.api.services.articles import ArticlesCRUD


router = APIRouter()


@router.get("", response_model=list[Article], status_code=200)
async def get_articles(session: AsyncSession = Depends(get_db)):
    return await ArticlesCRUD.list_article(session=session)


@router.get("/{article_id}", response_model=ArticleDetail, status_code=200)
async def get_article(article_id: int, session: AsyncSession = Depends(get_db)):
    return await ArticlesCRUD.detail_article(session=session, article_id=article_id)


@router.post("", response_model=Article, status_code=201)
async def create_article(
    article_data: Annotated[ArticleCreate, Depends()],
    session: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await ArticlesCRUD.create_article(
        session=session, article_data=article_data, user=user
    )


@router.delete("/{article_id}", status_code=204)
async def delete_article(article_id: int, session: AsyncSession = Depends(get_db)):
    return await ArticlesCRUD.delete_article(article_id=article_id, session=session)


@router.put("/{article_id}", response_model=Article)
async def update_article(
    article_id: int,
    article_data: Annotated[ArticleCreate, Depends()],
    session: AsyncSession = Depends(get_db),
):
    return await ArticlesCRUD.update_article(
        article_id=article_id, article_data=article_data, session=session
    )


@router.post("/{article_id}/comment", response_model=Comment)
async def create_comment(
    article_id: int,
    comment_data: Annotated[CommentCreate, Depends()],
    session: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await CommentsService.create_comment(
        article_id=article_id, comment_data=comment_data, session=session, user=user
    )
