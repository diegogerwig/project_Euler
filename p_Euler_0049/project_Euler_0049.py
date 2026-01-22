"""
Project Euler Problem 49: Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

Find the other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import math

def get_primes(limit):
    """Sieve of Eratosthenes to return a list of primes up to limit."""
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False
                
    return [i for i, prime in enumerate(is_prime) if prime]

def solve_prime_permutations():
    print("Searching for arithmetic sequences of permuated primes...")
    
    # 1. Get all 4-digit primes (1000 to 9999)
    primes = [p for p in get_primes(10000) if p >= 1000]
    
    # 2. Group primes by their permutation signature
    permutations = {}
    for p in primes:
        signature = "".join(sorted(str(p)))
        if signature not in permutations:
            permutations[signature] = []
        permutations[signature].append(p)
        
    # 3. Find Arithmetic Sequences within groups
    for key, group in permutations.items():
        if len(group) < 3:
            continue
        
        # Check every pair to see if a third term exists
        n = len(group)
        for i in range(n):
            for j in range(i + 1, n):
                p1 = group[i]
                p2 = group[j]
                
                step = p2 - p1
                p3 = p2 + step
                
                # Check if the third term is in the group
                if p3 in group:
                    concatenated = f"{p1}{p2}{p3}"
                    
                    # Filter: Separate the example from the solution
                    if p1 == 1487:
                        print(f"[Example Found] Sequence: {p1}, {p2}, {p3} (Step: {step})")
                    else:
                        print("\n" + "="*40)
                        print("★ SOLUTION FOUND ★")
                        print(f"Sequence: {p1}, {p2}, {p3}")
                        print(f"Step (Difference): {step}")
                        print(f"Concatenated 12-digit Answer: {concatenated}")
                        print("="*40 + "\n")
                        return # Stop after finding the solution

if __name__ == "__main__":
    solve_prime_permutations()