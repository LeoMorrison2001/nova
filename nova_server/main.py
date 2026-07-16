"""应用入口：使用 `uv run main.py` 启动服务。"""

import os

import uvicorn

from src.app import app


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8001"))
    uvicorn.run(app, host="127.0.0.1", port=port)
