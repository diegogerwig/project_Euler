"""
Project Euler Problem 70: Totient Permutation

Find the value of n < 10^7 for which phi(n) is a permutation of n 
and the ratio n/phi(n) produces a minimum.

Strategy:
Minimize n/phi(n) => Minimize product(p / (p-1)).
This implies n should be composed of very large primes.
We look for n = p1 * p2 where p1, p2 are close to sqrt(10^7) approx 3162.
"""

def get_primes(start, end):
    """Generates primes in a specific range using a simple check or sieve."""
    primes = []
    # Sieve of Eratosthenes is overkill for a small range, but efficient enough
    # Let's just do a simple primality check for this range (2000-5000)
    for num in range(start, end):
        is_p = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_p = False
                break
        if is_p:
            primes.append(num)
    return primes

def is_permutation(a, b):
    """Checks if two numbers are permutations of each other."""
    # Sorting strings is the easiest way in Python (O(D log D))
    return sorted(str(a)) == sorted(str(b))

def solve_totient_permutation():
    limit = 10**7
    
    # We look for primes around sqrt(10^7) ~= 3162.
    # A range of 2000 to 5000 ensures we cover all candidates 
    # that multiply to ~10^7 with minimized ratio.
    primes = get_primes(2000, 5000)
    
    min_ratio = float('inf')
    result_n = 0
    
    # Iterate through pairs of primes
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            p1 = primes[i]
            p2 = primes[j]
            
            n = p1 * p2
            
            if n > limit:
                # Since p2 increases, any further p2 will also result in n > limit
                break
            
            # Formula for phi when n = p1 * p2
            phi = (p1 - 1) * (p2 - 1)
            
            # Check permutation first (it's a strict filter)
            if is_permutation(n, phi):
                ratio = n / phi
                if ratio < min_ratio:
                    min_ratio = ratio
                    result_n = n
                    # Optional debug
                    # print(f"New best: n={n} (p1={p1}, p2={p2}), ratio={ratio:.6f}")

    print(f"Value of n producing minimum ratio: {result_n}")

if __name__ == "__main__":
    solve_totient_permutation()