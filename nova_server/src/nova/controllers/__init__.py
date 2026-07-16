from fastapi import APIRouter

from src.nova.controllers.agent import router as agent_router
from src.nova.controllers.permission import router as permission_router


api_router = APIRouter()
api_router.include_router(permission_router)
api_router.include_router(agent_router)
