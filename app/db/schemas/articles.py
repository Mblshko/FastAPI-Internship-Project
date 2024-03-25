from pydantic import BaseModel, ConfigDict


class ArticleBase(BaseModel):
    title: str
    content: str
    is_published: bool


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    author_id: int
