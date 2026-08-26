# bruteforce.py

import time
import itertools
from biscuit.hashing import compute_hash
import biscuit.output as output_templates
import biscuit.config
import biscuit.constants as CONST
import biscuit.calculations
from biscuit.config import CHARSET


# Valdates given arguments, searches for the missing ones before executing the attack
def validate_args(target_hash: str, algorithm: str, charset: str, min_length: int, max_length) -> bool:
    missing = []

    if not target_hash:
        missing.append("--hash")
    if not algorithm:
        missing.append("--algorithm")
    if not charset:
        missing.append("--charset")
    if not min_length:
        missing.append("--min-length")
    if not max_length:
        missing.append("--max-length")

    if missing:
        print(f"error: the following arguments are required: {", ".join(missing)}")
        return False
    else:
        return True


# Progress refresh system. Refreshes every <biscuit.config.REFRESH_INTERVAL> seconds
def refresh_progress(combinations_tested: int, total_combinations: int, execution_stopwatch: float, last_refresh_time: float, previous_combinations_tested: int, stop: bool):
    time_elapsed = output_templates.time_formatter(time.perf_counter() - execution_stopwatch)

    if stop:
        speed = 0
    else:
        speed = biscuit.calculations.speed_calc(combinations_tested, previous_combinations_tested, last_refresh_time, time.perf_counter())

    if stop:
        time_remaining = output_templates.time_formatter(0)
    else:
        time_remaining = output_templates.time_formatter(biscuit.calculations.time_remaining_calc(combinations_tested, total_combinations, speed))
    
    print("\033[6A\r" + output_templates.bruteforce_mode_progress(combinations_tested, total_combinations, time_elapsed, speed, time_remaining) + "\n")
    
    return time.perf_counter(), combinations_tested


# Main brute-force attack function
def main(target_hash: str, algorithm: str, charset: str, min_length: int, max_length: int, output: str):
    if not validate_args(target_hash, algorithm, charset, min_length, max_length):
        return

    print(CONST.HEADER)
    print(output_templates.bruteforce_mode_parameters(target_hash, algorithm, charset, min_length, max_length, output) + "\n")
    

    # Performance counters
    execution_stopwatch = time.perf_counter()
    last_refresh_time = time.perf_counter()

    target_digest = bytes.fromhex(target_hash)

    combinations_tested = 0
    total_combinations = 0
    time_elapsed = "None"
    speed = 0
    time_remaining = "None"
    previous_combinations_tested = 0

    # Total combinations
    print(output_templates.state("Computing the total amount of combinations..."))

    for length in range(min_length, max_length+1):
        total_combinations += len(CHARSET[charset])**length

    print("\033[1A\r" + output_templates.bruteforce_mode_progress(combinations_tested, total_combinations, time_elapsed, speed, time_remaining) + "\n")
    print(output_templates.state("In progress..."))

    for length in range(min_length, max_length+1):
        for candidate in itertools.product(CHARSET[charset], repeat=length):
            candidate = "".join(candidate)
            combinations_tested += 1

            # Success, end of execution
            if target_digest == compute_hash("".join(candidate), algorithm):
                last_refresh_time, previous_combinations_tested = refresh_progress(combinations_tested, total_combinations, execution_stopwatch, last_refresh_time, previous_combinations_tested, True)
                print(output_templates.state("Finished"))
                print(output_templates.result(True, candidate))
                return

            # Progress refresh. Checks whether <biscuit.config.REFRESH_INTERVAL> seconds passed to refresh the progress.
            if time.perf_counter() - last_refresh_time >= biscuit.config.REFRESH_INTERVAL:
                last_refresh_time, previous_combinations_tested = refresh_progress(combinations_tested, total_combinations, execution_stopwatch, last_refresh_time, previous_combinations_tested, False)
                print(output_templates.state("In progress..."))

    # Unsuccess, end of execution
    last_refresh_time, previous_candidates_tested = refresh_progress(combinations_tested, total_combinations, execution_stopwatch, last_refresh_time, previous_combinations_tested, True)
    print(output_templates.state("Finished"))
    print(output_templates.result(False, None))
    print()