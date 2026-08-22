VERSION = "0.1.0"

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

TOOL_DESCRIPTION = "Offline password hash auditing & recovery tool"
MODE_DICTIONARY_DESCRIPTION = "Test passwords from a wordlist against a target hash"
MODE_BRUTEFORCE_DESCRIPTION = "Generate and test passwords across a defined keyspace"
MODE_SPRAY_DESCRIPTION = "Test a password against multiple target hashes"
MODE_HASHGEN_DESCRIPTION = "Generate a hash from a given password and algorithm"
HELP_DESCRIPTION = "Show this help message and exit"

ARGS_HASH_DESCRIPTION = "Target password hash"
ARGS_ALGORITHM_DESCRIPTION = "Algorithm used to hash candidates"
ARGS_WORDLIST_DESCRIPTION= "Wordlist to use. Default: NCSC-100K"
ARGS_OUTPUT_DESCRIPTION = "Output file. If omitted, print results to the terminal"
ARGS_CHARSET_DESCRIPTION = "Character set used to generate hash candidates"
ARGS_MIN_LENGTH_DESCRIPTION = "Minimum password length of generated hash candidates"
ARGS_MAX_LENGTH_DESCRIPTION = "Maximum password length of generated hash candidates"
ARGS_PASSWORD_DESCRIPTION = "Password to hash"