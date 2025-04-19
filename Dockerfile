# 使用Python 3.13官方镜像作为基础镜像
FROM python:3.13-slim

# 设置工作目录
WORKDIR /weather

# 设置环境变量

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 复制项目文件
COPY . /weather/

# 安装依赖
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 8080

# 设置启动命令
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8080"]