# bruteforce.py

import time
import biscuit.output as output_templates
import biscuit.constants as CONST


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


# Main brute-force attack function
def main(target_hash: str, algorithm: str, charset: str, min_length: int, max_length: int, output: str):
    if not validate_args(target_hash, algorithm, charset, min_length, max_length):
        return

    print(CONST.HEADER)
    print(output_templates.bruteforce_mode_parameters(target_hash, algorithm, charset, min_length, max_length, output))

    # Performance counters
    execution_stopwatch = time.perf_counter()
    last_refresh_time = time.perf_counter()