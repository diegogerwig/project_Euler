"""
Project Euler Problem 87: Prime Power Triples

How many numbers below fifty million can be expressed as the sum of 
a prime square, prime cube, and prime fourth power?

Formula: N = p1^2 + p2^3 + p3^4 < 50,000,000
"""

def get_primes(n):
    """Sieve of Eratosthenes to find primes up to n."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def solve_prime_power_triples():
    limit = 50000000
    
    # Upper bound for the square term: sqrt(50,000,000) approx 7071
    # This covers all primes needed for the cube and fourth power as well.
    max_prime = int(limit**0.5) + 1
    primes = get_primes(max_prime)
    
    # We use a set to store found numbers to automatically handle duplicates
    # Alternatively, a boolean array [False] * limit is also very fast/memory efficient here.
    found_numbers = set()
    
    # Iterate through primes for the fourth power (p3)
    # 2^4 = 16. p3^4 must be < limit
    for p3 in primes:
        term3 = p3 ** 4
        if term3 >= limit:
            break
            
        # Iterate through primes for the cube (p2)
        for p2 in primes:
            term2 = p2 ** 3
            current_sum_2 = term3 + term2
            if current_sum_2 >= limit:
                break
                
            # Iterate through primes for the square (p1)
            for p1 in primes:
                term1 = p1 ** 2
                total = current_sum_2 + term1
                
                if total >= limit:
                    break
                
                found_numbers.add(total)
                
    print(f"Count of numbers below {limit}: {len(found_numbers)}")

if __name__ == "__main__":
    solve_prime_power_triples()