
from pydantic import BaseModel

class TrafficData(BaseModel):
    timestamp: int
    mode: str
    lane_A: int
    lane_B: int
    lane_C: int
    lane_D: int
