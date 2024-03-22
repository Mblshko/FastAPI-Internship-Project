from pydantic import BaseModel

from fastapi import Query

from typing import Annotated


class Item(BaseModel):
    name: str
    description: Annotated[str | None, Query(max_length=100)] = None
    price: float
    tax: float | None = None
