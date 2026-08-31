# dictionary.py

from pathlib import Path
import time
from biscuit.hashing import compute_hash
import biscuit.config
import biscuit.output as output_templates
import biscuit.calculations
import biscuit.constants


# Valdates given arguments, searches for the missing ones before executing the attack
def validate_args(target_hash: str, algorithm: str) -> bool:
    missing = []

    if not target_hash:
        missing.append("--hash")
    if not algorithm:
        missing.append("--algorithm")

    if missing:
        print(f"error: the following arguments are required: {", ".join(missing)}")
        return False
    else:
        return True


# Progress refresh system. Refreshes every <biscuit.config.REFRESH_INTERVAL> seconds
def refresh_progress(candidates_tested: int, total_candidates: int, execution_stopwatch: float, last_refresh_time: float, previous_candidates_tested: int, stop: bool):
    time_elapsed = output_templates.time_formatter(time.perf_counter() - execution_stopwatch)

    if stop:
        speed = 0
    else:
        speed = biscuit.calculations.speed_calc(candidates_tested, previous_candidates_tested, last_refresh_time, time.perf_counter())

    if stop:
        time_remaining = output_templates.time_formatter(0)
    else:
        time_remaining = output_templates.time_formatter(biscuit.calculations.time_remaining_calc(candidates_tested, total_candidates, speed))
    
    print("\033[6A\r" + output_templates.dictionary_mode_progress(candidates_tested, total_candidates, time_elapsed, speed, time_remaining) + "\n")
    
    return time.perf_counter(), candidates_tested


# Main dictionary attack function
def main(target_hash: str, algorithm: str, wordlist: str, output: str) -> None:
    # Validate given arguments
    if not validate_args(target_hash, algorithm):
        return

    # Convert target hexadecimal hash into binary code
    try:
        target_digest = bytes.fromhex(target_hash)
    except ValueError:
        print("error: hash must contain an even number of hexadecimal digits")
        return

    # Wordlist path handler
    if wordlist in biscuit.config.WORDLISTS:
        wordlist_path = biscuit.config.WORDLISTS[wordlist]["PATH"]
        wordlist_length = biscuit.config.WORDLISTS[wordlist]["LENGTH"]
    elif Path(wordlist).exists():
        wordlist_path = Path(wordlist)
        wordlist_length = len(wordlist_path.read_text().splitlines())
    else:
        print("error: wordlist was not found")
        return

    # Print app's header and mode's initial parameters
    print(biscuit.constants.HEADER)
    print(output_templates.dictionary_mode_parameters(target_hash, algorithm, wordlist, output) + "\n")

    # Performance counters
    execution_stopwatch = time.perf_counter()
    last_refresh_time = time.perf_counter()

    # Initialize essential variables
    candidates_tested = 0
    total_candidates = wordlist_length
    time_elapsed = "None"
    speed = 0
    time_remaining = "None"
    previous_candidates_tested = 0
    
    print("\033[1A\r" + output_templates.dictionary_mode_progress(candidates_tested, total_candidates, time_elapsed, speed, time_remaining) + "\n")
    print(output_templates.state("In progress..."))

    # Wordlist file opening
    with wordlist_path.open(mode="r", encoding="UTF-8") as file:
        # Password -> Hash -> Compare loop
        for candidate in file:
            candidate = candidate.strip("\r\n")
            candidates_tested += 1

            # Success, end of execution
            if target_digest == compute_hash(candidate, algorithm):
                last_refresh_time, previous_candidates_tested = refresh_progress(candidates_tested, total_candidates, execution_stopwatch, last_refresh_time, previous_candidates_tested, True)
                print(output_templates.state("Finished"))
                print(output_templates.result(True, candidate))
                return

            # Progress refresh. Checks whether <biscuit.config.REFRESH_INTERVAL> seconds passed to refresh the progress.
            if time.perf_counter() - last_refresh_time >= biscuit.config.REFRESH_INTERVAL:
                last_refresh_time, previous_candidates_tested = refresh_progress(candidates_tested, total_candidates, execution_stopwatch, last_refresh_time, previous_candidates_tested, False)
                print(output_templates.state("In progress..."))

        # Unsuccess, end of execution
        last_refresh_time, previous_candidates_tested = refresh_progress(candidates_tested, total_candidates, execution_stopwatch, last_refresh_time, previous_candidates_tested, True)
        print(output_templates.state("Finished"))
        print(output_templates.result(False, None))
        print()