from fastapi import APIRouter

from src.nova.controllers.health import router as health_router
from src.nova.controllers.home import router as home_router


api_router = APIRouter()
api_router.include_router(home_router)
api_router.include_router(health_router)
