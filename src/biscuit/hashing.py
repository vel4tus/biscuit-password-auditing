import hashlib

def compute_hash(password: str, algorithm: str) -> bytes:
    return hashlib.new(algorithm, password.encode()).digest()