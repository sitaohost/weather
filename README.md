# 天气查询API

基于FastAPI的天气查询服务，数据来源于魅族天气API
> ⚠️ 本项目仅供学习和研究使用，项目使用的天气数据API来自魅族天气服务，若被告知需停止共享与使用，本人将及时删除此页面与整个项目

## 功能特点

- 支持全国城市天气查询
- 提供实时天气、未来3天预报
- 包含空气质量和生活指数

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行服务

```bash
python app/main.py
或
fastapi run app/main.py --host 0.0.0.0 --port 8080
```

服务启动后访问：http://localhost:8080/docs 查看API文档

### API示例

```bash
curl "http://localhost:8080/api/v1/weather/?city=长沙"
```

响应数据包含：
- 实时天气（温度、湿度、风向等）
- 空气质量（AQI、PM2.5等）
- 未来3天预报
- 生活指数和建议

## 技术栈

- Python 3.13
- FastAPI
- aiohttp
