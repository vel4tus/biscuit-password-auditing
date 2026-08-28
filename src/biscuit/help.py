# help.py

import biscuit.constants as CONST
from biscuit.config import WORDLISTS, DEFAULT_WORDLIST, HASH_ALGORITHMS, CHARSET


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

{CONST.MODE_DICTIONARY_DESCRIPTION}

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


def bf_help() -> str:
    return f'''usage: biscuit bruteforce [-h] --hash <HASH> --algorithm
                          {{{",".join(HASH_ALGORITHMS)}}} --charset 
                          {{{",".join(CHARSET)}}}
                          --min-length <MIN_LENGTH> --max-length <MAX_LENGTH>
                          [--output <OUTPUT>]

{CONST.MODE_BRUTEFORCE_DESCRIPTION}


Required arguments:
  -H, --hash <HASH>     {CONST.ARGS_HASH_DESCRIPTION}

  -a, --algorithm {{{",".join(HASH_ALGORITHMS)}}}
                        {CONST.ARGS_ALGORITHM_DESCRIPTION}

  -c, --charset {{{",".join(CHARSET)}}}
                        {CONST.ARGS_CHARSET_DESCRIPTION}

  -m, --min-length <MIN_LENGTH>
                        {CONST.ARGS_MIN_LENGTH_DESCRIPTION}

  -M, --max-length <MAX_LENGTH>
                        {CONST.ARGS_MAX_LENGTH_DESCRIPTION}

Optional arguments:
  -o, --output <PATH>   {CONST.ARGS_OUTPUT_DESCRIPTION}

  -h, --help            {CONST.HELP_DESCRIPTION}

examples:
  biscuit bruteforce --hash <hash> --algorithm sha256 --charset alphanumeric
  biscuit bruteforce --hash <hash> --algorithm sha256 --charset alphanumeric --min-length 4 --max-length 8
  biscuit bruteforce --hash <hash> --algorithm sha256 --charset alphanumeric --min-length 6 --max-length 6'''


def hg_help() -> str:
    return f'''usage: biscuit hash-gen [-h] --password <PASSWORD> --algorithm
                        {{{",".join(HASH_ALGORITHMS)}}}

Generate a hash from a given password and algorithm.

Required arguments:
  -P, --password <PASSWORD>
                        {CONST.ARGS_PASSWORD_DESCRIPTION}
  -a, --algorithm {{{",".join(HASH_ALGORITHMS)}}}
                        {CONST.ARGS_ALGORITHM_DESCRIPTION}

Optional arguments:
  -h, --help            {CONST.HELP_DESCRIPTION}

Examples:
  biscuit hash-gen --password <PASSWORD> --algorithm sha256'''