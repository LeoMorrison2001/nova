"""智能体模块的 HTTP 接口。"""

from fastapi import APIRouter


router = APIRouter(prefix="/agents", tags=["agents"])
