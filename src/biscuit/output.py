# output.py

import time


def header() -> str:
    return '''
██████╗ ██╗███████╗ ██████╗██╗   ██╗██╗████████╗
██╔══██╗██║██╔════╝██╔════╝██║   ██║██║╚══██╔══╝
██████╔╝██║███████╗██║     ██║   ██║██║   ██║
██╔══██╗██║╚════██║██║     ██║   ██║██║   ██║
██████╔╝██║███████║╚██████╗╚██████╔╝██║   ██║
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝

Offline password hash auditing & recovery tool

! Authorized use only !
'''


def state(state: str) -> str:
    return f'''\033[2KState: {state}'''

def result(success: bool, password: str | None) -> str:
    if success:
        return f'''Result: Password found\nPassword: {password}'''

    if not success:
        return f'''Result: Password not found'''

# ==============================
#    Dictionary mode outputs   
# ==============================

def dictionary_mode_parameters(target_hash: str, algorithm: str, wordlist: str, output: str) -> str:
    return f'''MODE:       Dictionary Attack
HASH:       {target_hash}
ALGORITHM:  {algorithm}
WORDLIST:   {wordlist}
OUTPUT:     {output}'''


def dictionary_mode_progress(candidates_tested: int, total_candidates: int, time_elapsed: str, speed: int, time_remaining: str) -> str:
    return f'''\033[2KCandidates tested:  {candidates_tested} / {total_candidates}
\033[2KTime elapsed:       {time_elapsed}
\033[2KSpeed:              {speed} candidates/sec
\033[2KTime remaining:     {time_remaining}'''


def dictionary_mode_state(state: str) -> str:
    return f'''\033[2KState: {state}'''

def dictionary_mode_result(success: bool, password: str | None) -> str:
    if success:
        return f'''Result: Password found\nPassword: {password}'''

    if not success:
        return f'''Result: Password not found'''


# ==============================
#    Brute-force mode outputs 
# ==============================


def bruteforce_mode_parameters(target_hash: str, algorithm: str, charset: str, min_length: int, max_length: int, output: str):
    return f'''MODE:       Brute-force Attack
HASH:       {target_hash}
ALGORITHM:  {algorithm}
CHARSET:    {charset}
LENGTH:     {f"{min_length}" if min_length == max_length else f"{min_length}-{max_length}"}
OUTPUT:     {output}'''


def bruteforce_mode_progress(combinations_tested: int, total_combinations: int, time_elapsed: str, speed: int, time_remaining: str) -> str:
    return f'''\033[2KCombinations tested:  {combinations_tested} / {total_combinations}
\033[2KTime elapsed:         {time_elapsed}
\033[2KSpeed:                {speed} candidates/sec
\033[2KTime remaining:       {time_remaining}'''


def time_formatter(time: int | float | None) -> str:
    if time is None:
        return "None"
    elif time < 60:
        return f"{time:.0f} sec"
    elif time < 60*60:
        return f"{time//60:.0f} min {time%60:.0f} sec"
    else:
        return f"{time//(60*60):.0f} h {(time%(60*60))//60:.0f} min {time%60:.0f} sec"
    