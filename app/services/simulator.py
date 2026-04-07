import time
import random
import numpy as np

class TrafficSimulator:
    def __init__(self):
        self.arrival_modes = {
            "peak": (20, 45),
            "normal": (10, 30),
            "low": (3, 12),
        }

    def get_mode(self):
        hour = int(time.strftime("%H"))
        if 7 <= hour <= 9 or 17 <= hour <= 20:
            return "peak"
        elif 23 <= hour or hour < 6:
            return "low"
        return "normal"

    def generate(self):
        mode = self.get_mode()
        low, high = self.arrival_modes[mode]

        lane_A = np.random.poisson(random.randint(low, high))
        lane_B = np.random.poisson(random.randint(low, high))
        lane_C = np.random.poisson(random.randint(low, high))
        lane_D = np.random.poisson(random.randint(low, high))

        return {
            "timestamp": int(time.time()),
            "mode": mode,
            "lane_A": int(lane_A),
            "lane_B": int(lane_B),
            "lane_C": int(lane_C),
            "lane_D": int(lane_D),
        }