from hashing import compute_hash

def hash_gen(password: str, algorithm: str) -> None:
    print(compute_hash(password, algorithm).hex())