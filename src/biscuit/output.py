# output.py

import time
import biscuit.constants as CONST
from biscuit.config import WORDLISTS, DEFAULT_WORDLIST, HASH_ALGORITHMS

# ==============================
#         Common outputs        
# ==============================

def help() -> str:
    return f'''usage: biscuit [-h] <MODE> ...

Biscuit v{CONST.VERSION}

Offline password hash auditing & recovery tool

! Authorized use only !

Modes:

  Attacks:
    dictionary, dict  {CONST.MODE_DICTIONARY_DESCRIPTION}
    brute-force, bf   {CONST.MODE_BRUTEFORCE_DESCRIPTION}
    spray             {CONST.MODE_SPRAY_DESCRIPTION}

  Utilities:
    hash-gen, hg      {CONST.MODE_HASHGEN_DESCRIPTION}

Options:
  -h, --help          {CONST.HELP_DESCRIPTION}

Use 'biscuit <mode> --help' for more information about a specific mode.

Examples:
  biscuit dictionary --hash <HASH> --algorithm sha256
  biscuit brute-force --hash <HASH> --algorithm sha256 --charset alphanumeric --min-length 6 --max-length 8
  biscuit spray ...
  biscuit hash-gen --password <PASSWORD> --algorithm sha256'''


def dict_help() -> str:
    return f'''usage: biscuit dictionary [-h] --hash <HASH> --algorithm
                          {{{",".join(HASH_ALGORITHMS)}}}
                          [--wordlist <NAME|PATH>]
                          [--output <PATH>]

Test passwords from a wordlist against a target hash.

Built-in wordlists:
{"\n".join(WORDLISTS.keys())}

Default wordlist:
{DEFAULT_WORDLIST}

Required arguments:
  -H, --hash <HASH>     {CONST.ARGS_HASH_DESCRIPTION}
  -a, --algorithm {{{",".join(HASH_ALGORITHMS)}}}
                        {CONST.ARGS_ALGORITHM_DESCRIPTION}

Optional arguments:
  -w, --wordlist <NAME|PATH>
                        {CONST.ARGS_WORDLIST_DESCRIPTION}
  -o, --output <PATH>   {CONST.ARGS_OUTPUT_DESCRIPTION}

  -h, --help            {CONST.HELP_DESCRIPTION}

Examples:
  biscuit dictionary --hash <HASH> --algorithm sha256
  biscuit dictionary --hash <HASH> --algorithm sha256 --wordlist XATO-100K
  biscuit dictionary --hash <HASH> --algorithm sha256 --wordlist /path/to/wordlist.txt
  biscuit dictionary --hash <HASH> --algorithm sha256 --output /path/to/results.txt'''


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

# ==============================
#         Time formatter        
# ==============================

def time_formatter(time: int | float | None) -> str:
    if time is None:
        return "None"
    elif time < 60:
        return f"{time:.0f} sec"
    elif time < 60*60:
        return f"{time//60:.0f} min {time%60:.0f} sec"
    else:
        return f"{time//(60*60):.0f} h {(time%(60*60))//60:.0f} min {time%60:.0f} sec"
    