
from pydantic import BaseModel

class OptimizationResult(BaseModel):
    cycle_time: int
    traffic_pressure: dict
    signal_timing: dict
