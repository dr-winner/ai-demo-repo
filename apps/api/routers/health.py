from fastapi import APIRouter
from config import settings

router = APIRouter(tags=["health"])

@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "app": settings.PROJECT_NAME,
        "version": settings.APP_VERSION
    }
