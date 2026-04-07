import random
import time

def generate_traffic_data():
    return {
        "timestamp": int(time.time()),
        "lane_A": random.randint(5, 40),
        "lane_B": random.randint(5, 40),
        "lane_C": random.randint(5, 40),
        "lane_D": random.randint(5, 40)
    }