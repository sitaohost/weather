from pydantic import BaseModel
from typing import List, Optional, Dict, Any, Union

class WeatherResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Optional[Union[List[Dict[str, Any]], Dict[str, Any]]] = None