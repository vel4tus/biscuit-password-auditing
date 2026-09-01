import itertools
from biscuit.hashing import compute_hash
from biscuit.config import CHARSET

def bruteforce_engine(algorithm: str, charset: str, min_length: int, max_length: int):
    for length in range(min_length, max_length+1):
        for candidate in itertools.product(CHARSET[charset], repeat=length):
            candidate = "".join(candidate)
            candidate_digest = compute_hash(candidate, algorithm)
            yield candidate, candidate_digest, length