from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services.auth import current_active_user
from app.api.services.comments import CommentsService
from app.db import User
from app.db.base import get_db
from app.db.schemas.comments import Comment, CommentCreate

router = APIRouter()


@router.post("/{article_id}", response_model=Comment)
async def create_comment(
    article_id: int,
    comment_data: Annotated[CommentCreate, Depends()],
    session: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await CommentsService.create_comment(
        article_id=article_id, comment_data=comment_data, session=session, user=user
    )


@router.delete("/{article_id}", status_code=204)
async def delete_comment(
    comment_id: int,
    session: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await CommentsService.delete_comment(
        comment_id=comment_id, session=session, user=user
    )
