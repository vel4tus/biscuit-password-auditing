# CLI.py

import argparse
import biscuit.config
from biscuit.modes import dictionary, bruteforce, hashgen
import biscuit.output as output_templates
import biscuit.constants as CONST

# CLI implementation using argparse
parser = argparse.ArgumentParser(
    description="Offline password hash auditing & recovery tool", 
    color=False,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    add_help=False
    )

# Help menu
parser.add_argument("--help", "-h", action="store_true")

# Subparser for multiple biscuit.modes
subparsers = parser.add_subparsers(title="biscuit.modes", dest="mode", help=output_templates.help_output())

# Dicitonary attack parser
dictionary_parser = subparsers.add_parser(name="dictionary", aliases=["dict"], description=CONST.DICTIONARY_DESCRIPTION)
dictionary_parser.add_argument("--hash", "-H", help="Target password hash", required=True)
dictionary_parser.add_argument("--algorithm", "-a", help="Algorithm used to hash candidates", choices=biscuit.config.HASH_ALGORITHMS, required=True)
dictionary_parser.add_argument("--wordlist", "-w", help="Wordlist to use. Default: NCSC-100K", choices=biscuit.config.WORDLISTS, default="NCSC-100K")
dictionary_parser.add_argument("--output", "-o", help="Output file. If omitted, print results to the terminal", metavar="PATH")
# Salt support - WIP
# dictionary_parser.add_argument("--salt")
# dictionary_parser.add_argument("--salt-position", choices=["prefix", "suffix"], default="suffix")

# Brute-force attack parser
bruteforce_parser = subparsers.add_parser(name="brute-force", aliases=["bf"], description=CONST.BRUTEFORCE_DESCRIPTION)
bruteforce_parser.add_argument("--hash", "-H", help="Target password hash", required=True)
bruteforce_parser.add_argument("--algorithm", "-a", help="Algorithm used to hash candidates", choices=biscuit.config.HASH_ALGORITHMS, required=True)
bruteforce_parser.add_argument("--charset", "-c", required=True, choices=biscuit.config.CHARSET, help="Character set used to generate hash candidates")
bruteforce_parser.add_argument("--min-length", "-m", type=int, required=True, help="Minimum password length of generated hash candidates", dest="min_length")
bruteforce_parser.add_argument("--max-length", "-M", type=int, required=True, help="Maximum password length of generated hash candidates", dest="max_length")
bruteforce_parser.add_argument("--output", "-o", help="Output file. If omitted, print results to the terminal", metavar="PATH")
# Salt support - WIP
# dictionary_parser.add_argument("--salt")
# dictionary_parser.add_argument("--salt-position", choices=["prefix", "suffix"], default="suffix")

# Password spraying attack parser
spray_parser = subparsers.add_parser(name="spray", description=CONST.SPRAY_DESCRIPTION)

# Hash generation parser
hashgen_parser = subparsers.add_parser(name="hash-gen", aliases=["hg"], description=CONST.HASHGEN_DESCRIPTION)
hashgen_parser.add_argument("--password", "-P", help="Password to hash", required=True)
hashgen_parser.add_argument("--algorithm", "-a", help="Algorithm used to hash the password", choices=biscuit.config.HASH_ALGORITHMS, required=True)


def main():
    args = parser.parse_args()

    if args.help:
        print(output_templates.help_output())

    else:
        match args.mode:
            case "dictionary" | "dict":
                dictionary.main(args.hash, args.algorithm, args.wordlist, args.output)

            case "brute-force" | "bf":
                bruteforce.main(args.hash, args.algorithm, args.charset, args.min_length, args.max_length, args.output)

            case "spray":
                pass

            case "hash-gen" | "hg":
                hashgen.main(args.password, args.algorithm)
