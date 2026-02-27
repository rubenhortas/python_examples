#!/usr/bin/env python3

import concurrent.futures
import math
import os
import time

def _compute_factorial(n) -> str:
    _ = math.factorial(n)
    return f"Factorial of {n} computed."

def _main() -> None:
    numbers = [50000, 60000, 70000, 80000]

    print(f"Starting execution with {len(numbers)} tasks...")
    start_time = time.perf_counter()

    # By default, ProcessProolExecutor uses all CPU cores
    with concurrent.futures.ProcessPoolExecutor(max_workers=max(1, (os.cpu_count() or 1) - 1)) as executor:
        results = list(executor.map(_compute_factorial, numbers))

    end_time = time.perf_counter()

    for res in results:
        print(res)

    print(f"\nTotal time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    try:
        _main()
    except KeyboardInterrupt:
        pass
