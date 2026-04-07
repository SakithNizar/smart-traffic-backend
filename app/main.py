from fastapi import FastAPI
from app.services.simulator import generate_traffic_data
from app.services.optimizer import optimize_signal_timing

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smart Traffic System API running"}

@app.get("/traffic")
def get_traffic_data():
    return generate_traffic_data()

@app.get("/optimize")
def optimize():
    data = generate_traffic_data()
    timing = optimize_signal_timing(data)
    return {"input_data": data, "optimized_signal_timing": timing}