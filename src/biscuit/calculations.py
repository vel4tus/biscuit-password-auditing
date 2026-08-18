def speed_calc(candidates_tested: int, previous_candidates_tested: int, last_refresh_time: float, perf_counter: float) -> int:
    return int(f"{(candidates_tested-previous_candidates_tested)*(1/(perf_counter-last_refresh_time)):.0f}")

def time_remaining_calc(candidates_tested: int, total_candidates: int, speed: int) -> float | None:
    if speed == 0:
        return None
    
    return (total_candidates-candidates_tested)/speed