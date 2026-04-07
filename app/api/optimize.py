from fastapi import APIRouter
from app.services.simulator import TrafficSimulator
from app.services.optimizer import PressureOptimizer

router = APIRouter()
sim = TrafficSimulator()
optimizer = PressureOptimizer()

@router.get("/optimize")
def optimize():
    data = sim.generate()
    return {
        "traffic_data": data,
        "optimization": optimizer.compute(data)
    }