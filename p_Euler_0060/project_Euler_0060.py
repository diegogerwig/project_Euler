"""
Project Euler Problem 60: Prime Pair Sets

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
"""

import math

def is_prime_mr(n, k=5):
    """
    Miller-Rabin primality test for larger numbers.
    Perfect for checking concatenated primes like 123456789.
    """
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = 2 + _ # Deterministic enough for this range or use random
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def get_primes(limit):
    """Sieve of Eratosthenes"""
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    return [i for i, p in enumerate(sieve) if p]

def concat_prime_check(p1, p2):
    """Returns True if p1p2 and p2p1 are both prime."""
    # Math trick to concat without string conversion (faster)
    # But string conversion is cleaner in Python and fast enough here.
    s1 = str(p1)
    s2 = str(p2)
    
    if not is_prime_mr(int(s1 + s2)): return False
    if not is_prime_mr(int(s2 + s1)): return False
    return True

def solve_prime_pair_sets():
    # We search primes up to 10,000. The solution is typically within this range.
    limit = 10000
    primes = get_primes(limit)
    
    # Pre-filter: 2 and 5 cannot be part of a large set 
    # (because 'x2' is even and 'x5' is div by 5)
    if 2 in primes: primes.remove(2)
    if 5 in primes: primes.remove(5)
    
    min_sum = float('inf')
    
    # Memoization for valid pairs to avoid re-checking
    # pairs[p] = list of primes q > p that pair with p
    pairs_memo = {p: [] for p in primes}
    
    # We build the sets recursively
    def find_clique(current_clique):
        nonlocal min_sum
        
        # Pruning: If current sum already exceeds best found, stop.
        if sum(current_clique) >= min_sum:
            return

        # Goal check
        if len(current_clique) == 5:
            current_sum = sum(current_clique)
            if current_sum < min_sum:
                min_sum = current_sum
                print(f"New best set: {current_clique}, Sum: {min_sum}")
            return

        # Candidates are primes larger than the last element in clique
        last_p = current_clique[-1]
        
        # Try to extend using pre-calculated compatible pairs if available,
        # otherwise scan forward.
        # To make this fast, we only check 'p' that are compatible with 'last_p'
        # AND compatible with everyone else in current_clique.
        
        # Optimization: We only need to iterate through primes that pair with the 
        # *first* element of the clique (or any element), to reduce search space.
        # But for simplicity and correctness in DFS:
        
        start_index = primes.index(last_p) + 1
        
        for i in range(start_index, len(primes)):
            candidate = primes[i]
            
            # Pruning inside loop
            if sum(current_clique) + candidate * (5 - len(current_clique)) >= min_sum:
                # If adding this candidate (and hypothetical smallest subsequent candidates)
                # exceeds min_sum, we can stop this branch entirely because primes are sorted.
                return

            # Verify candidate against ALL numbers in current_clique
            all_compatible = True
            for p in current_clique:
                if not concat_prime_check(p, candidate):
                    all_compatible = False
                    break
            
            if all_compatible:
                find_clique(current_clique + [candidate])

    print("Searching for prime clique...")
    
    # Level 1: Iterate all primes as starting points
    for i, p in enumerate(primes):
        # Basic progress indicator
        # print(f"Checking start prime: {p}")
        find_clique([p])
        
        # Heuristic break: if p is becoming too large to be the SMALLEST member
        # of a minimal sum set.
        if p * 5 > min_sum: 
            break
            
    print(f"Lowest sum for a set of five primes: {min_sum}")

if __name__ == "__main__":
    solve_prime_pair_sets()