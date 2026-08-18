def speed_calc(candidates_tested: int, candidates_tested_temp: int, refresh_timestamp: float, perf_counter: float) -> int:
    return int(f"{(candidates_tested-candidates_tested_temp)*(1/(perf_counter-refresh_timestamp)):.0f}")

def time_remaining_calc(candidates_tested: int, total_candidates: int, speed: int) -> float | None:
    if speed == 0:
        return None
    
    return (total_candidates-candidates_tested)/speed