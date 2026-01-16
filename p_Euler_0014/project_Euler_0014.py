"""
Project Euler Problem 14: Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n -> n/2    (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

def solve_collatz():
    """
    Solves Project Euler Problem 14 using memoization (caching) 
    to optimize the calculation of chain lengths.
    """
    start_time = time.time()
    
    # Cache to store lengths of sequences we have already calculated.
    # Base case: The number 1 has a sequence length of 1.
    cache = {1: 1}

    def get_chain_length(n):
        """
        Recursive function to find the length of the Collatz chain for n.
        Uses the cache to retrieve previously calculated lengths to avoid
        redundant calculations.
        """
        # If we already know the answer for n, return it immediately
        if n in cache:
            return cache[n]

        # Apply the Collatz rules to find the next number in the sequence
        if n % 2 == 0:
            next_val = n // 2   # Even rule
        else:
            next_val = 3 * n + 1 # Odd rule

        # Recursive step: 
        # Length is 1 (current step) + length of the next value's chain
        length = 1 + get_chain_length(next_val)
        
        # Store the result in cache before returning
        cache[n] = length
        return length

    max_length = 0
    starting_number = 0
    limit = 1000000
    
    # Iterate through all starting numbers under one million
    for i in range(1, limit):
        length = get_chain_length(i)
        
        if length > max_length:
            max_length = length
            starting_number = i

    end_time = time.time()
    
    print(f"Problem: Find the starting number under {limit} with the longest chain.")
    print("-" * 50)
    print(f"Result: The starting number is {starting_number}")
    print(f"Chain length: {max_length}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    solve_collatz()