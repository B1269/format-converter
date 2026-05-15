"""
格式转换工具 - FastAPI后端
"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import convert, health, auth

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = FastAPI(
    title="格式转换工具 API",
    description="支持文档格式转换、图片处理、视频压缩等功能",
    version="1.0.0"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应该限制具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(health.router, prefix="/api", tags=["健康检查"])
app.include_router(convert.router, prefix="/api", tags=["文件转换"])
app.include_router(auth.router, prefix="/api/auth", tags=["用户认证"])


@app.get("/")
async def root():
    return {"message": "格式转换工具 API", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
