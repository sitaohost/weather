from fastapi import APIRouter
from .endpoints.weather import weather_router

api_router_v1 = APIRouter()
api_router_v1.include_router(weather_router, prefix="/weather", tags=["天气"])