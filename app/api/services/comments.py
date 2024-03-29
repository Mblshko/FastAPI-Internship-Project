from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete

from app.db import User, Comment
from app.db.schemas.comments import CommentCreate


class CommentsService:
    @staticmethod
    async def create_comment(
        session: AsyncSession, comment_data: CommentCreate, user: User, article_id: int
    ):
        data = comment_data.model_dump()
        data["user_id"] = user.id
        data["article_id"] = article_id
        comment = Comment(**data)
        session.add(comment)
        await session.commit()
        return comment

    @staticmethod
    async def delete_comment(session: AsyncSession, comment_id: int, user: User):
        stmt = delete(Comment).where(Comment.id == comment_id)
        if Comment.user_id == user.id:
            await session.execute(stmt)
            await session.commit()
