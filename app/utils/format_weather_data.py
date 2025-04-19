from typing import Dict, Any, List


async def format_weather_data(raw_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    格式化天气数据，提取关键信息并优化展示
    """
    if not raw_data or len(raw_data) == 0:
        return {}

    weather_info = raw_data[0]

    # 提取基本信息
    basic_info = {
        "城市": f"{weather_info.get('provinceName', '')} {weather_info.get('city', '')} {weather_info.get('region', '')}",
        "更新时间": weather_info.get("realtime", {}).get("time", ""),
    }

    # 提取实时天气
    realtime = weather_info.get("realtime", {})
    current_weather = {
        "天气": realtime.get("weather", ""),
        "温度": f"{realtime.get('temp', '')}°C",
        "体感温度": f"{realtime.get('sendibleTemp', '')}°C",
        "湿度": f"{realtime.get('sD', '')}%",
        "风向": realtime.get("wD", ""),
        "风力": realtime.get("wS", ""),
    }

    # 提取空气质量
    pm25 = weather_info.get("pm25", {})
    air_quality = {
        "空气质量": pm25.get("quality", ""),
        "AQI": pm25.get("aqi", ""),
        "PM2.5": pm25.get("pm25", ""),
        "PM10": pm25.get("pm10", ""),
        "更新时间": pm25.get("upDateTime", ""),
    }

    # 提取天气预报
    forecast = []
    for day in weather_info.get("weathers", [])[:3]:  # 只取未来3天
        forecast.append(
            {
                "日期": f"{day.get('date', '')} {day.get('week', '')}",
                "天气": day.get("weather", ""),
                "温度": f"{day.get('temp_night_c', '')}°C ~ {day.get('temp_day_c', '')}°C",
                "日出": day.get("sun_rise_time", ""),
                "日落": day.get("sun_down_time", ""),
            }
        )

    # 提取生活指数
    life_index = {}
    for index in weather_info.get("indexes", []):
        life_index[index.get("name", "")] = {
            "等级": index.get("level", ""),
            "建议": index.get("content", ""),
        }

    # 组合最终结果
    formatted_data = {
        "基本信息": basic_info,
        "实时天气": current_weather,
        "空气质量": air_quality,
        "天气预报": forecast,
        "生活指数": life_index,
    }

    return formatted_data
