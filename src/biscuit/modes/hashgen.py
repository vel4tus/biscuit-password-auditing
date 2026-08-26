# hashgen.py

from biscuit.hashing import compute_hash


# Valdates given arguments, searches for the missing ones before executing the attack
def validate_args(password: str, algorithm: str) -> bool:
    missing = []

    if not password:
        missing.append("--hash")
    if not algorithm:
        missing.append("--algorithm")

    if missing:
        print(f"error: the following arguments are required: {", ".join(missing)}")
        return False
    else:
        return True


def main(password: str, algorithm: str) -> None:
    if not validate_args(password, algorithm):
        return

    print(compute_hash(password, algorithm).hex())