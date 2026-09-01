import time
import biscuit.output as output_templates
from biscuit.engines.bruteforce_engine import bruteforce_engine
import biscuit.calculations
import biscuit.constants as CONST
import biscuit.config


def dictionary_benchmark_parameters(algorithm: str, wordlist: str) -> str:
    return f'''MODE:       Dictionary Attack [Benchmark Mode]
ALGORITHM:  {algorithm}
WORDLIST:   {wordlist}'''


def dictionary_benchmark_progress(candidates_tested: int, total_candidates: int, time_elapsed: str, speed: int, time_remaining: str) -> str:
    return f'''\033[2KCandidates tested:  {candidates_tested} / {total_candidates}
\033[2KTime elapsed:       {time_elapsed}
\033[2KSpeed:              {speed} candidates/sec
\033[2KTime remaining:     {time_remaining}'''


def bruteforce_benchmark_parameters(algorithm: str, charset: str, min_length: int, max_length: int):
    return f'''MODE:       Brute-force Attack [Benchmark Mode]
ALGORITHM:  {algorithm}
CHARSET:    {charset}
LENGTH:     {f"{min_length}" if min_length == max_length else f"{min_length}-{max_length}"}'''


def bruteforce_benchmark_progress(combinations_tested: int, total_combinations: int, progress: float, time_elapsed: str, speed: int, avg_speed: int, length: int):
    return f'''\033[2KCombinations tested:  {combinations_tested} / {total_combinations}
\033[2KProgress:             {progress}%
\033[2KTime elapsed:         {time_elapsed}
\033[2KSpeed:                {speed} combinations/sec
\033[2KAverage speed:        {avg_speed} combinations/sec
\033[2KCurrent length:       {length}'''


def bruteforce_benchmark_result(total_combinations: int, execution_time: str, avg_speed: int):
    return f'''\033[2KCombinations:    {total_combinations}
\033[2KExecution time:  {execution_time}
\033[2KAverage speed:   {avg_speed} combinations/sec'''


def bruteforce_benchmark(algorithm: str, charset: str, min_length: int, max_length: int):

    # Initialize essential variables
    combinations_tested = 0
    previous_combinations_tested = 0
    avg_speed = 0

    # Calculate the quantity of all combinations
    total_combinations = biscuit.calculations.total_combinations_calc(charset, min_length, max_length)

    # Performance counters
    execution_stopwatch = time.perf_counter()
    last_refresh_time = time.perf_counter()

    # Print app's header and mode's initial parameters
    print(CONST.HEADER)
    print(bruteforce_benchmark_parameters(algorithm, charset, min_length, max_length) + "\n")

    # Print mode's initial progress and current state
    print(bruteforce_benchmark_progress(combinations_tested, total_combinations, 0, "None", 0, 0, 0) + "\n")
    print(output_templates.state("In progress..."))

    # Execute the attack. For each length the iteration is performed separately. If min_length and max_length are equal, perform the iteration once.
    for _, _, length in bruteforce_engine(algorithm, charset, min_length, max_length):

        combinations_tested += 1

        # Progress refresh. Check whether <biscuit.config.REFRESH_INTERVAL> seconds passed to refresh the progress.
        if time.perf_counter() - last_refresh_time >= biscuit.config.REFRESH_INTERVAL:
            current_time = time.perf_counter()
            progress = round(combinations_tested/total_combinations*100)
            time_elapsed = output_templates.time_formatter(current_time - execution_stopwatch)
            speed = biscuit.calculations.speed_calc(combinations_tested, previous_combinations_tested, last_refresh_time, current_time)
            avg_speed = round(combinations_tested / (current_time - execution_stopwatch))

            print("\033[8A\033[J\r" + bruteforce_benchmark_progress(combinations_tested, total_combinations, progress, time_elapsed, speed, avg_speed, length) + "\n")
            print(output_templates.state(f"In progress..."))

            previous_combinations_tested = combinations_tested
            last_refresh_time = current_time

    # End of execution
    execution_time = time.perf_counter() - execution_stopwatch
    avg_speed = round(combinations_tested / execution_time)
    print("\033[8A\033[J\r" + bruteforce_benchmark_result(total_combinations, f"{execution_time:.6f} sec", avg_speed) + "\n")
    print(output_templates.state(f"Finished"))