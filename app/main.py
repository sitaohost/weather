import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api.v1.router import api_router_v1
from core.config import project_root  # 从配置模块导入

app = FastAPI(title="天气查询API", description="提供城市天气查询服务", version="1.0.0")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(api_router_v1, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "天气查询API [版本1.0.0]"}


if __name__ == "__main__":
    print("项目根目录：", project_root)
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    # fastapi run app/main.py --host 0.0.0.0 --port 8080
