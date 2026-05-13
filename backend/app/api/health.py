"""
健康检查API
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """健康检查"""
    return {
        "status": "healthy",
        "service": "format-converter-api",
        "version": "1.0.0"
    }
