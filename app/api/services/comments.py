from sqlalchemy.ext.asyncio import AsyncSession

from app.db import User, Article
from app.db.schemas.comments import CommentCreate


class CommentsService:
    @staticmethod
    async def create_comment(
        session: AsyncSession, text: CommentCreate, user: User, article: Article
    ):
        pass

    @staticmethod
    async def delete_comment(session: AsyncSession, comment_id: int):
        pass
