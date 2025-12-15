from pydantic import BaseModel

class FloodData(BaseModel):
    water_level: float
    rainfall: float
