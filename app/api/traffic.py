
from fastapi import APIRouter
from app.services.simulator import TrafficSimulator

router = APIRouter()
sim = TrafficSimulator()

@router.get("/traffic")
def get_traffic():
    return sim.generate
