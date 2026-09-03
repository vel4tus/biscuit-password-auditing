# bruteforce_engine.py

import itertools
import concurrent.futures
from biscuit.hashing import compute_hash
from biscuit.config import CHARSET
import biscuit.config


def worker(target_digest: bytes | None, chunk: list, algorithm: str) -> tuple[str | None, int]:
    combinations_tested = 0

    for candidate in chunk:
        combinations_tested += 1

        candidate_digest = compute_hash(candidate, algorithm)

        if target_digest == candidate_digest:
            return candidate, combinations_tested

    return None, combinations_tested


def bruteforce_engine(target_digest: bytes | None, algorithm: str, charset: str, min_length: int, max_length: int):

    with concurrent.futures.ProcessPoolExecutor() as executor:
        chunk = []
        futures = []

        for length in range(min_length, max_length+1):

            for candidate in itertools.product(CHARSET[charset], repeat=length):
                candidate = "".join(candidate)
                chunk.append(candidate)

                if len(chunk) >= biscuit.config.CHUNK_SIZE:
                    futures.append(executor.submit(worker, target_digest, chunk, algorithm))
                    chunk = []

                    if len(futures) >= biscuit.config.CHUNK_MAX:
                        for future in concurrent.futures.as_completed(futures):
                            yield future.result()[0], future.result()[1], length

                        futures = []

            if chunk:
                futures.append(executor.submit(worker, target_digest, chunk, algorithm))
                chunk = []

            if len(futures) >= biscuit.config.CHUNK_MAX:
                for future in concurrent.futures.as_completed(futures):
                    yield future.result()[0], future.result()[1], length

                futures = []
