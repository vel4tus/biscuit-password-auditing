# test.py

import itertools
import string
import time

num = 0
length = 8

charset = string.digits
combinations = len(charset) ** length

stopwatch = time.perf_counter()
timestamp = time.perf_counter()
eta_min = 0
speed_sec_value = 0
speed_sec = 0

for i in itertools.product(charset, repeat=length):
    num += 1

    if time.perf_counter() - timestamp > 0.1:
        speed_sec = (num - speed_sec_value) * 10
        eta_min = (combinations - num) / speed_sec / 60

        speed_sec_value = num
        
        print(f"\rCombinations generated: {num}/{combinations} | Time elapsed: {time.perf_counter() - stopwatch:.0f} sec | ETA: {eta_min:.2f} min | Speed: {speed_sec} combinations/sec", end="", flush=True)
        timestamp = time.perf_counter()

print()
print(num)
print(combinations)