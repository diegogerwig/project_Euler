"""
Project Euler Problem 77: Prime Summations

What is the first value which can be written as the sum of primes 
in over five thousand different ways?

Method: Dynamic Programming (Coin Change variant using Primes).
"""

def get_primes(n):
    """Generate a list of primes up to n using Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def solve_prime_summations():
    target_ways = 5000
    # Guess a limit. Partitions grow fast, so 100 is likely enough.
    limit = 100
    
    while True:
        primes = get_primes(limit)
        
        # ways[i] will store the number of ways to make sum i using primes
        ways = [0] * (limit + 1)
        ways[0] = 1
        
        # Dynamic Programming: Iterate through each prime "coin"
        for p in primes:
            for j in range(p, limit + 1):
                ways[j] += ways[j - p]
        
        # Check if we found the answer
        found = False
        for i in range(limit + 1):
            if ways[i] > target_ways:
                print(f"First value written as sum of primes in over {target_ways} ways: {i}")
                print(f"Number of ways: {ways[i]}")
                found = True
                return
        
        # If not found, increase limit and try again (unlikely to be needed for 5000)
        limit *= 2

if __name__ == "__main__":
    solve_prime_summations()