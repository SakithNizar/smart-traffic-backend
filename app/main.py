from fastapi import FastAPI
from app.api import traffic, optimize
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(traffic.router)
app.include_router(optimize.router)

@app.get("/")
def root():
    return {"message": "Smart Traffic Optimization API is running"}