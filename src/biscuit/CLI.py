# CLI.py

import argparse
import config
from modes import dictionary, bruteforce, hashgen

# CLI implementation using argparse
parser = argparse.ArgumentParser(
    description="Offline password hash auditing & recovery tool", 
    color=False,
    formatter_class=argparse.RawDescriptionHelpFormatter
    )

# Subparser for multiple modes
subparsers = parser.add_subparsers(title="modes", dest="mode" ,required=True)

# Dicitonary attack parser
dictionary_parser = subparsers.add_parser(name="dictionary", description="Test passwords from a wordlist against a target hash", help="Dictionary Attack")
dictionary_parser.add_argument("--hash", help="Target password hash", required=True)
dictionary_parser.add_argument("--algorithm", help="Algorithm used to hash candidates", choices=config.HASH_ALGORITHMS, required=True)
dictionary_parser.add_argument("--wordlist", help="Wordlist to use. Default: NCSC-100K", choices=config.WORDLISTS, default="NCSC-100K")
dictionary_parser.add_argument("--output", help="Output file. If omitted, print results to the terminal", metavar="PATH")
# Salt support - WIP
# dictionary_parser.add_argument("--salt")
# dictionary_parser.add_argument("--salt-position", choices=["prefix", "suffix"], default="suffix")

# Brute-force attack parser
bruteforce_parser = subparsers.add_parser(name="brute-force", description="Generate and test passwords across a defined keyspace", help="Brute-force Attack")
bruteforce_parser.add_argument("--hash", help="Target password hash", required=True)
bruteforce_parser.add_argument("--algorithm", help="Algorithm used to hash candidates", choices=config.HASH_ALGORITHMS, required=True)
bruteforce_parser.add_argument("--charset", help="Character set used to generate hash candidates")
bruteforce_parser.add_argument("--min-length", help="Minimum password length of generated hash candidates", dest="min_length")
bruteforce_parser.add_argument("--max-length", help="Maximum password length of generated hash candidates", dest="max_length")
bruteforce_parser.add_argument("--output", help="Output file. If omitted, print results to the terminal", metavar="PATH")
# Salt support - WIP
# dictionary_parser.add_argument("--salt")
# dictionary_parser.add_argument("--salt-position", choices=["prefix", "suffix"], default="suffix")

# Password spraying attack parser
spray_parser = subparsers.add_parser(name="spray", description="Tests a password against multiple target hashes", help="Password Spraying Attack")

# Hash generation parser
hashgen_parser = subparsers.add_parser(name="hash-gen", description="Generate a hash with a given password and algorithm", help="Hash generator")
hashgen_parser.add_argument("--password", help="Password to hash", required=True)
hashgen_parser.add_argument("--algorithm", help="Algorithm used to hash the password", choices=config.HASH_ALGORITHMS, required=True)


def main():
    args = parser.parse_args()

    match args.mode:
        case "dictionary":
            dictionary.main(args.hash, args.algorithm, args.wordlist, args.output)
        case "brute-force":
            bruteforce.main(args.hash, args.algorithm, args.charset, args.min_length, args.max_length, args.output)
        case "spray":
            pass
        case "hash-gen":
            hashgen.main(args.password, args.algorithm)
