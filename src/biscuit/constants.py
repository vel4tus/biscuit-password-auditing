# constants.py

VERSION = "0.1.0"
TOOL_DESCRIPTION = "Offline password hash auditing & recovery tool"

HEADER = f'''
██████╗ ██╗███████╗ ██████╗██╗   ██╗██╗████████╗
██╔══██╗██║██╔════╝██╔════╝██║   ██║██║╚══██╔══╝
██████╔╝██║███████╗██║     ██║   ██║██║   ██║
██╔══██╗██║╚════██║██║     ██║   ██║██║   ██║
██████╔╝██║███████║╚██████╗╚██████╔╝██║   ██║
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝  v{VERSION}

Offline password hash auditing & recovery tool

! Authorized use only !
'''

MODE_DICTIONARY_DESCRIPTION = "Test passwords from a wordlist against a target hash"
MODE_BRUTEFORCE_DESCRIPTION = "Generate and test passwords candidates across a defined keyspace"
MODE_SPRAY_DESCRIPTION = "Test a password against multiple target hashes"
MODE_HASHGEN_DESCRIPTION = "Generate a hash from a given password and algorithm"

HELP_DESCRIPTION = "Show this help message and exit"

ARGS_HASH_DESCRIPTION = "Target password hash"
ARGS_ALGORITHM_DESCRIPTION = "Algorithm used to hash candidates"
ARGS_WORDLIST_DESCRIPTION= "Wordlist to use. Can be either a built-in wordlist or a path"
ARGS_OUTPUT_DESCRIPTION = "Path to the output file"
ARGS_CHARSET_DESCRIPTION = "Character set used to generate hash candidates"
ARGS_MIN_LENGTH_DESCRIPTION = "Minimum password length of generated hash candidates"
ARGS_MAX_LENGTH_DESCRIPTION = "Maximum password length of generated hash candidates"
ARGS_PASSWORD_DESCRIPTION = "Password to hash"