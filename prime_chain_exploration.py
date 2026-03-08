#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.

import multiprocessing
import time
import gmpy2

def hunt_worker(start_offset, stride, limit, min_length):
    results = []
    for x in range(start_offset, limit, stride):
        # Use gmpy2 for ultra-fast primality testing
        if not gmpy2.is_prime(x):
            continue

        chain = [x]
        current = x

        while True:
            next_val = (3 * current + 1) // 2
            if gmpy2.is_prime(next_val):
                chain.append(next_val)
                current = next_val
            else:
                break

        if len(chain) >= min_length:
            results.append(chain)
            print(f"! L{len(chain)} Found!: {chain[0]} -> ... -> {chain[-1]}")

    return results

def parallel_collatz_hunt_gmpy2(limit, min_length=10):
    num_cores = multiprocessing.cpu_count()
    
    # Mathematical truth: length L chains always start at 2^L * k - 1
    step = 2 ** min_length
    base_start = step - 1

    tasks = []
    for i in range(num_cores):
        start_offset = base_start + (i * step)
        stride = step * num_cores
        tasks.append((start_offset, stride, limit, min_length))

    print(f"Hunting L{min_length}+ up to {limit} using {num_cores} cores with gmpy2...")
    start_time = time.time()

    with multiprocessing.Pool(num_cores) as pool:
        pool.starmap(hunt_worker, tasks)

    print(f"Hunt completed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    # Dive into the 1 trillion (10**12) space
    parallel_collatz_hunt_gmpy2(limit=10**12, min_length=9)


# In[ ]:




