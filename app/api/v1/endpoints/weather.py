from fastapi import APIRouter, Query, HTTPException
from services.weather import get_weather_by_city
from schemas.weather import WeatherResponse
from utils.format_weather_data import format_weather_data

weather_router = APIRouter()


@weather_router.get("/", response_model=WeatherResponse)
async def get_weather(city: str = Query(..., description="城市名称，如：长沙")):
    """
    获取指定城市的天气信息
    """
    weather_data, error = await get_weather_by_city(city)
    
    if error:
        return WeatherResponse(success=False, message=error)
    
    if not weather_data:
        return WeatherResponse(success=False, message="未获取到天气数据")
    
    # 格式化天气数据
    formatted_data = await format_weather_data(weather_data)
    
    return WeatherResponse(success=True, data=formatted_data)
