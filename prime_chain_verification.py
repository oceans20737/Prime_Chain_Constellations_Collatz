#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.

from sympy import isprime

def generate_collatz_prime_chain(start_val):
    """
    Generates a prime chain under the Collatz-type mapping:
        f(x) = (3x + 1) / 2
    The chain continues as long as each term remains prime.

    Parameters:
        start_val (int): The starting value of the chain.

    Returns:
        list[int]: A list of consecutive primes forming the chain.
    """
    chain = []
    current = start_val

    # Continue generating terms while the current value is prime
    while isprime(current):
        chain.append(current)
        current = (3 * current + 1) // 2

    return chain


# Example: Verify and display a discovered Length-9 chain
if __name__ == "__main__":
    n0 = 35014031359
    chain = generate_collatz_prime_chain(n0)

    print(f"Collatz prime chain starting from {n0} (Length: {len(chain)}):")
    print(" -> ".join(map(str, chain)))


# In[ ]:




