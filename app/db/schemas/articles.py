from app.db.schemas.comments import Comment

from pydantic import BaseModel, ConfigDict


class ArticleBase(BaseModel):
    title: str
    content: str
    is_published: bool


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    """Response"""

    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int


class ArticleDetail(Article):
    comments: list[Comment]
