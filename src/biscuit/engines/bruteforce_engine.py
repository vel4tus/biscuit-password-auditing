# bruteforce_engine.py

import itertools
import concurrent.futures
from biscuit.hashing import compute_hash
from biscuit.config import CHARSET


def worker(chunk: list, algorithm: str):
    results = []

    for candidate in chunk:
        candidate_digest = compute_hash(candidate, algorithm)
        results.append((candidate, candidate_digest))

    return results


def bruteforce_engine(algorithm: str, charset: str, min_length: int, max_length: int):

    with concurrent.futures.ProcessPoolExecutor() as executor:
        chunk = []
        futures = []

        for length in range(min_length, max_length+1):

            for candidate in itertools.product(CHARSET[charset], repeat=length):
                candidate = "".join(candidate)
                chunk.append(candidate)

                if len(chunk) >= 10000:
                    futures.append(executor.submit(worker, chunk, algorithm))
                    chunk = []

                    if len(futures) >= 4:
                        for future in concurrent.futures.as_completed(futures):
                            for candidate, candidate_digest in future.result():
                                yield candidate, candidate_digest, length

                        futures = []

        if chunk:
            futures.append(executor.submit(worker, chunk, algorithm))

        for future in concurrent.futures.as_completed(futures):
            for candidate, candidate_digest in future.result():
                yield candidate, candidate_digest, max_length
