# calculations.py
from biscuit.config import CHARSET


def speed_calc(candidates_tested: int, previous_candidates_tested: int, last_refresh_time: float, perf_counter: float) -> int:
    return int(f"{(candidates_tested-previous_candidates_tested)*(1/(perf_counter-last_refresh_time)):.0f}")


def time_remaining_calc(candidates_tested: int, total_candidates: int, speed: int) -> float | None:
    if speed == 0:
        return None
    
    return (total_candidates-candidates_tested)/speed


def total_combinations_calc(charset: str, min_length: int, max_length: int) -> int:
    total_combinations = 0

    for length in range(min_length, max_length+1):
        total_combinations += len(CHARSET[charset])**length

    return total_combinations