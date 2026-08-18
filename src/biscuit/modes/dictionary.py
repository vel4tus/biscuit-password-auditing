# dictionary.py

from pathlib import Path
import time
from hashing import compute_hash
import config
import output as output_templates
import calculations


def refresh_progress(candidates_tested: int, total_candidates: int, execution_stopwatch: float, refresh_timestamp: float, candidates_tested_temp: int, stop: bool):
    time_elapsed = output_templates.time_formatter(time.perf_counter() - execution_stopwatch)

    if stop:
        speed = 0
    else:
        speed = calculations.speed_calc(candidates_tested, candidates_tested_temp, refresh_timestamp, time.perf_counter())

    if stop:
        time_remaining = output_templates.time_formatter(0)
    else:
        time_remaining = output_templates.time_formatter(calculations.time_remaining_calc(candidates_tested, total_candidates, speed))
    
    print("\033[4A\r" + output_templates.dictionary_mode_progress(candidates_tested, total_candidates, time_elapsed, speed, time_remaining))
    
    return [time.perf_counter(), candidates_tested]


# Main dictionary attack function
def dictionary_attack(target_hash: str, algorithm: str, wordlist: str, output: str) -> None:
    print(output_templates.header())
    print(output_templates.dictionary_mode_parameters(target_hash, algorithm, wordlist, output) + "\n")

    # Wordlist path handler
    if wordlist in config.WORDLISTS:
        wordlist_path = config.WORDLISTS[wordlist]["PATH"]
        wordlist_length = config.WORDLISTS[wordlist]["LENGTH"]
    elif Path(wordlist).exists():
        wordlist_path = Path(wordlist)
        wordlist_length = len(wordlist_path.read_text().splitlines())
    else:
        print("Error: Output file not found")
        return
    
    # Performance counters
    execution_stopwatch = time.perf_counter()
    refresh_timestamp = time.perf_counter()

    # Wordlist file opening
    with wordlist_path.open(mode="r", encoding="UTF-8") as file:
        target_digest = bytes.fromhex(target_hash)

        candidates_tested = 0
        total_candidates = wordlist_length
        time_elapsed = "None"
        speed = 0
        time_remaining = "None"
        candidates_tested_temp = 0

        print(output_templates.dictionary_mode_progress(candidates_tested, total_candidates, time_elapsed, speed, time_remaining))

        # Password -> Hash -> Compare loop
        for candidate in file:
            candidate = candidate.strip("\r\n")
            candidates_tested += 1

            if target_digest == compute_hash(candidate, algorithm):
                refresh_progress(candidates_tested, total_candidates, execution_stopwatch, refresh_timestamp, candidates_tested_temp, True)
                print(f"\nPassword found: {candidate}")
                return

            # refresh progress
            if time.perf_counter() - refresh_timestamp >= config.REFRESH_INTERVAL:
                [refresh_timestamp, candidates_tested_temp] = refresh_progress(candidates_tested, total_candidates, execution_stopwatch, refresh_timestamp, candidates_tested_temp, False)

        refresh_progress(candidates_tested, total_candidates, execution_stopwatch, refresh_timestamp, candidates_tested_temp, True)

        print()