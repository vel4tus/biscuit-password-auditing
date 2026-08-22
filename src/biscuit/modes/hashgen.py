# hashgen.py

from biscuit.hashing import compute_hash


def main(password: str, algorithm: str) -> None:
    print(compute_hash(password, algorithm).hex())