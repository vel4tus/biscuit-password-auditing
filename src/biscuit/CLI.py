# CLI.py

import argparse
import biscuit.config
from biscuit.modes import dictionary, bruteforce, hashgen
from biscuit.config import DEFAULT_WORDLIST
import biscuit.help as help

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
subparsers = parser.add_subparsers(title="biscuit.modes", dest="mode")

# Dicitonary attack parser
dictionary_parser = subparsers.add_parser(name="dictionary", aliases=["dict"], add_help=False)
dictionary_parser.add_argument("--help", "-h", action="store_true", dest="dict_help")
dictionary_parser.add_argument("--hash", "-H")
dictionary_parser.add_argument("--algorithm", "-a", choices=biscuit.config.HASH_ALGORITHMS)
dictionary_parser.add_argument("--wordlist", "-w", default=DEFAULT_WORDLIST)
dictionary_parser.add_argument("--output", "-o")
# Salt support - WIP
# dictionary_parser.add_argument("--salt")
# dictionary_parser.add_argument("--salt-position", choices=["prefix", "suffix"], default="suffix")

# Brute-force attack parser
bruteforce_parser = subparsers.add_parser(name="brute-force", aliases=["bf"], add_help=False)
bruteforce_parser.add_argument("--help", "-h", action="store_true", dest="bf_help")
bruteforce_parser.add_argument("--hash", "-H")
bruteforce_parser.add_argument("--algorithm", "-a", choices=biscuit.config.HASH_ALGORITHMS)
bruteforce_parser.add_argument("--charset", "-c", choices=biscuit.config.CHARSET)
bruteforce_parser.add_argument("--min-length", "-m", type=int)
bruteforce_parser.add_argument("--max-length", "-M", type=int)
bruteforce_parser.add_argument("--output", "-o", metavar="PATH")
# Salt support - WIP
# dictionary_parser.add_argument("--salt")
# dictionary_parser.add_argument("--salt-position", choices=["prefix", "suffix"], default="suffix")

# Password spraying attack parser
spray_parser = subparsers.add_parser(name="spray", add_help=False)

# Hash generation parser
hashgen_parser = subparsers.add_parser(name="hash-gen", aliases=["hg"], add_help=False)
hashgen_parser.add_argument("--help", "-h", action="store_true", dest="hg_help")
hashgen_parser.add_argument("--password", "-P")
hashgen_parser.add_argument("--algorithm", "-a", choices=biscuit.config.HASH_ALGORITHMS)


def main():
    args = parser.parse_args()

    if args.help or not args.mode:
        print(help.help())

    else:
        match args.mode:
            case "dictionary" | "dict":
                if args.dict_help:
                    print(help.dict_help())
                else:
                    dictionary.main(args.hash, args.algorithm, args.wordlist, args.output)

            case "brute-force" | "bf":
                if args.bf_help:
                    print(help.bf_help())
                else:
                    bruteforce.main(args.hash, args.algorithm, args.charset, args.min_length, args.max_length, args.output)

            case "spray":
                pass

            case "hash-gen" | "hg":
                if args.hg_help:
                    print(help.hg_help())
                else:
                    hashgen.main(args.password, args.algorithm)
