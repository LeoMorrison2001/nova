from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter(tags=["example"])


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home() -> str:
    """提供一个可在浏览器中直接打开的测试页。"""
    return """
    <!doctype html>
    <html lang="zh-CN">
      <head><meta charset="utf-8"><title>Nova Server</title></head>
      <body>
        <h1>Nova Server 正在运行</h1>
        <ul>
          <li><a href="/health">健康检查：/health</a></li>
          <li><a href="/docs">交互式 API 文档：/docs</a></li>
          <li><a href="/api/hello?name=Nova">示例 API：/api/hello?name=Nova</a></li>
        </ul>
      </body>
    </html>
    """


@router.get("/api/hello")
async def hello(name: str = "World") -> dict[str, str]:
    """示例接口：可通过查询参数传入 name。"""
    return {"message": f"Hello, {name}!"}
