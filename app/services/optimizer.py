class PressureOptimizer:

    def __init__(self):
        self.min_green = 10
        self.max_green = 60
        self.cycle_time = 120

    def compute(self, data):
        lanes = {
            "A": data["lane_A"],
            "B": data["lane_B"],
            "C": data["lane_C"],
            "D": data["lane_D"],
        }

        total = sum(lanes.values()) or 1

        # Calculate pressure (proportional traffic load)
        pressure = {
            lane: count / total for lane, count in lanes.items()
        }

        # Allocate signal time
        timing = {}
        for lane, p in pressure.items():
            raw_time = p * self.cycle_time
            bounded_time = max(self.min_green, min(self.max_green, raw_time))
            timing[lane] = round(bounded_time, 1)

        return {
            "cycle_time": self.cycle_time,
            "traffic_pressure": pressure,
            "signal_timing": timing
        }