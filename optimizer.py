def optimize_signal_timing(data):
    lanes = {
        "A": data["lane_A"],
        "B": data["lane_B"],
        "C": data["lane_C"],
        "D": data["lane_D"]
    }

    total = sum(lanes.values()) or 1
    cycle_time = 120

    timing = {
        lane: round((count / total) * cycle_time, 1)
        for lane, count in lanes.items()
    }

    return timing