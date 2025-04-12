from app.api.routers import main_router
from app.core.config import settings
from fastapi import FastAPI

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
)
app.include_router(
    router=main_router,
    prefix=settings.api_prefix,
)
