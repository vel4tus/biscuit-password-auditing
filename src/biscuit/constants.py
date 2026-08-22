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
DICTIONARY_DESCRIPTION = "Test passwords from a wordlist against a target hash"
BRUTEFORCE_DESCRIPTION = "Generate and test passwords across a defined keyspace"
SPRAY_DESCRIPTION = "Test a password against multiple target hashes"
HASHGEN_DESCRIPTION = "Generate a hash from a given password and algorithm"
HELP_DESCRIPTION = "Show this help message and exit"