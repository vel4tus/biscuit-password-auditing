# bruteforce.py

import time
import biscuit.output as output_templates
import biscuit.constants as CONST

# Main brute-force attack function
def main(target_hash: str, algorithm: str, charset: str, min_length: int, max_length: int, output: str):
    print(CONST.HEADER)
    print(output_templates.bruteforce_mode_parameters(target_hash, algorithm, charset, min_length, max_length, output))

    # Performance counters
    execution_stopwatch = time.perf_counter()
    last_refresh_time = time.perf_counter()