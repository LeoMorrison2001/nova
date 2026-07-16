# Nova Server

目录结构：

```text
src/
├── app.py          # 创建 FastAPI 应用、注册路由
└── nova/
    ├── routers/     # 路由层：接收 HTTP 请求
    ├── services/    # 业务层：处理业务规则
    └── repositories/# 数据层：读写数据库
```

启动开发服务：

```powershell
uv run main.py
```

启动后在浏览器打开：

- http://127.0.0.1:8001/
- http://127.0.0.1:8001/docs

默认端口为 `8001`。如需指定其他端口：

```powershell
$env:PORT = 8080
uv run main.py
```
