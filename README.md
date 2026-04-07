# Smart Traffic System (Basic Version)

## 🚦 Overview
A simple backend that simulates traffic data and calculates basic green-light timing using proportional algorithms.

## ✅ Features
- Simulated traffic data (no sensors needed)
- Basic optimization engine
- FastAPI backend with two endpoints

## 📡 Endpoints
### `/traffic`
Returns:
- Random values for lanes A, B, C, D
- Timestamp

### `/optimize`
- Generates traffic data
- Calculates signal timing

## ▶️ Run the Server

### Step 1 — Install dependencies

### Step 2 — Start the backend

Visit:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/traffic
- http://127.0.0.1:8000/optimize