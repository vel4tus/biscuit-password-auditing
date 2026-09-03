# bruteforce.py

import time
import itertools
from biscuit.hashing import compute_hash
import biscuit.output as output_templates
import biscuit.config
import biscuit.constants as CONST
import biscuit.calculations
import biscuit.help
from biscuit.config import CHARSET
from biscuit.benchmark import bruteforce_benchmark
from biscuit.engines.bruteforce_engine import bruteforce_engine


# Valdate given arguments, searche for the missing ones before executing the attack
def validate_attack_args(target_hash: str, algorithm: str, charset: str, min_length: int, max_length) -> bool:
    # Required: target_hash, algorithm, charset, min_length, max_length
    # Not allowed: target_hash, output

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

    # Print error if not validated and stop execution, else proceed
    if missing:
        print(f"error: the following arguments are required: {", ".join(missing)}")
        return False
    else:
        return True


def validate_benchmark_args(target_hash: str, algorithm: str, charset: str, min_length: int, max_length: int, output: str) -> bool:
    # Required: algorithm, charset, min_length, max_length
    # Not allowed: target_hash, output

    missing_args = []
    not_allowed_args = []

    if not algorithm:
        missing_args.append("algorithm")
    if not charset:
        missing_args.append("charset")
    if not min_length:
        missing_args.append("min_length")
    if not max_length:
        missing_args.append("max_length")
    if target_hash:
        not_allowed_args.append("target_hash")
    if output:
        not_allowed_args.append("output")

    # Print error if not validated
    if missing_args:
        print(f"error: the following arguments are required: {", ".join(missing_args)}")
    if not_allowed_args:
        print(f"error: the following arguments are not allowed: {", ".join(not_allowed_args)}")

    # Stop execution if not validated, else proceed
    if missing_args or not_allowed_args:
        return False
    else:
        return True


# Progress refresh system. Refresh every <biscuit.config.REFRESH_INTERVAL> seconds
def refresh_progress(combinations_tested: int, total_combinations: int, execution_stopwatch: float, last_refresh_time: float, previous_combinations_tested: int, length: int, stop: bool):
    current_time = time.perf_counter()
    time_elapsed = output_templates.time_formatter(current_time - execution_stopwatch)

    if stop:
        speed = 0
    else:
        speed = biscuit.calculations.speed_calc(combinations_tested, previous_combinations_tested, last_refresh_time, current_time)

    if stop:
        time_remaining = output_templates.time_formatter(0)
    else:
        time_remaining = output_templates.time_formatter(biscuit.calculations.time_remaining_calc(combinations_tested, total_combinations, speed))
    
    print("\033[7A\033[J\r" + output_templates.bruteforce_mode_progress(combinations_tested, total_combinations, time_elapsed, speed, time_remaining, length) + "\n")
    
    return current_time, combinations_tested


def bruteforce_attack(target_hash: str, algorithm: str, charset: str, min_length: int, max_length: int, output: str):

    # Convert target hexadecimal hash into binary code
    try:
        target_digest = bytes.fromhex(target_hash)
    except ValueError:
        print("error: hash must contain an even number of hexadecimal digits")
        return

    # Initialize essential variables
    combinations_tested = 0
    previous_combinations_tested = 0

    # Calculate the quantity of all combinations
    total_combinations = biscuit.calculations.total_combinations_calc(charset, min_length, max_length)

    # Performance counters
    execution_stopwatch = time.perf_counter()
    last_refresh_time = time.perf_counter()
    
    # Print app's header and mode's initial parameters
    print(CONST.HEADER)
    print(output_templates.bruteforce_mode_parameters(target_hash, algorithm, charset, min_length, max_length, output) + "\n")

    # Print mode's initial progress and current state
    print(output_templates.bruteforce_mode_progress(combinations_tested, total_combinations, "None", 0, "None", 0) + "\n")
    print(output_templates.state("In progress..."))

    # Execute the attack. For each length the iteration is performed separately. If min_length and max_length are equal, perform the iteration once.
    for candidate, combinations_tested_chunk, length in bruteforce_engine(target_digest, algorithm, charset, min_length, max_length):

        combinations_tested += combinations_tested_chunk
    
        # Success, end of execution
        if candidate:
            last_refresh_time, previous_combinations_tested = refresh_progress(combinations_tested, total_combinations, execution_stopwatch, last_refresh_time, previous_combinations_tested, length, True)
            print(output_templates.state("Finished"))
            print(output_templates.result(True, candidate))
            return

        # Progress refresh. Check whether <biscuit.config.REFRESH_INTERVAL> seconds passed to refresh the progress.
        if time.perf_counter() - last_refresh_time >= biscuit.config.REFRESH_INTERVAL:
            last_refresh_time, previous_combinations_tested = refresh_progress(combinations_tested, total_combinations, execution_stopwatch, last_refresh_time, previous_combinations_tested, length, False)
            print(output_templates.state(f"In progress..."))

    # Unsuccess, end of execution
    last_refresh_time, previous_candidates_tested = refresh_progress(combinations_tested, total_combinations, execution_stopwatch, last_refresh_time, previous_combinations_tested, max_length, True)
    print(output_templates.state("Finished"))
    print(output_templates.result(False, None))
    print()


# Dispatcher
def main(target_hash: str, algorithm: str, charset: str, min_length: int, max_length: int, output: str, show_help: bool, benchmark: bool) -> None:

    # Help
    if show_help:
        print(biscuit.help.bf_help())
        return

    # Benchmark
    if benchmark:
        if validate_benchmark_args(target_hash, algorithm, charset, min_length, max_length, output):
            bruteforce_benchmark(algorithm, charset, min_length, max_length)
            return
        else:
            return

    # Attack
    if not benchmark:
        if validate_attack_args(target_hash, algorithm, charset, min_length, max_length):
            bruteforce_attack(target_hash, algorithm, charset, min_length, max_length, output)
            return
        else:
            return