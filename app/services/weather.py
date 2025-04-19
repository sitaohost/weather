import aiohttp
import json
from core.config import project_root


async def load_city_map() -> dict:
    """加载城市ID映射"""
    # project_root = Path(__file__).parent.parent.parent
    city_file_path = project_root / "data" / "cityIds.json"

    with open(city_file_path, "r", encoding="utf-8") as f:
        cityIds = json.load(f)
    city_map = {city["countyname"].strip(): city["areaid"] for city in cityIds}
    return city_map


async def get_weather_by_city(city_name: str):
    """根据城市名称获取天气信息（异步版本）"""
    city_map = await load_city_map()

    try:
        area_id = city_map[city_name]
    except KeyError:
        return None, f"未找到'{city_name}'对应的区域ID"

    url = f"http://aider.meizu.com/app/weather/listWeather?cityIds={area_id}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

                if int(data["code"]) != 200:
                    return None, data["message"]

                return data["value"], None
    except Exception as e:
        return None, f"获取天气数据失败: {str(e)}"
