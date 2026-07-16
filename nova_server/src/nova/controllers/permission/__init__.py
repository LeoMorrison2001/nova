"""权限模块的 HTTP 接口。"""

from fastapi import APIRouter


router = APIRouter(prefix="/permissions", tags=["permissions"])
