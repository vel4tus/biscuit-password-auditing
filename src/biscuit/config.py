# config.py

'''
Internal Biscuit configuration

DO NOT modify this file unless you know what you're doing.
Modifying this file may result into unexpected behaviour and potentially break the tool.
'''


from pathlib import Path
import string


# Package's paths
PACKAGE_DIR = Path(__file__).parent
WORDLISTS_DIR = PACKAGE_DIR / "wordlists"


# Supported hash algorithms
HASH_ALGORITHMS = [
    "md5",
    "sha1",
    "sha256",
    "sha384",
    "sha512"
    ]


# Character sets
# The tool uses ASCII character set by default.
CHARSET = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "letters": string.ascii_letters,
    "alphanumeric": string.ascii_letters + string.digits,
    "special": string.punctuation,
    "all": string.ascii_letters + string.digits + string.punctuation
}


# Built-in wordlists
# To use an external wordlist, provide its path with the corresponding argument (--wordlist <PATH>).
WORDLISTS = {
    "NCSC-100K": {
        "PATH": WORDLISTS_DIR / "NCSC-100K.txt",
        "LENGTH": 99840
        },
    "XATO-10K": {
        "PATH" : WORDLISTS_DIR / "XATO-10K.txt",
        "LENGTH": 10000
        },
    "XATO-100K": {
        "PATH" : WORDLISTS_DIR / "XATO-100K.txt",
        "LENGTH": 100000
        },
    "XATO-1M": {
        "PATH" : WORDLISTS_DIR / "XATO-1M.txt",
        "LENGTH": 1000000
        },
    "XATO-5M": {
        "PATH" : WORDLISTS_DIR / "XATO-5M.txt",
        "LENGTH": 5189454
        }
}


# Default wordlist
# Currently cannot be changed
DEFAULT_WORDLIST = "NCSC-100K"


# Output refresh interval (in sec)
# Lower values may reduce execution performance.
# Common values: 0.1, 0.5, 1.0
REFRESH_INTERVAL = 0.1