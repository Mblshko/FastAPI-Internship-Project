from fastapi import FastAPI

from app.api.routers.articles import router as articles_router

app = FastAPI()
app.include_router(router=articles_router)
