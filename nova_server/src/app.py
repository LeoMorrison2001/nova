from fastapi import FastAPI

from src.nova.routers import api_router


def create_app() -> FastAPI:
    """创建并配置 FastAPI 应用。"""
    app = FastAPI(
        title="Nova Server",
        description="一个可直接运行的 FastAPI 项目骨架。",
        version="0.1.0",
    )
    app.include_router(api_router)
    return app


app = create_app()
