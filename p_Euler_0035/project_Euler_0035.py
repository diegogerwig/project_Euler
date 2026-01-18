"""
Project Euler Problem 35: Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.

How many circular primes are there below one million?
"""

def solve_circular_primes():
    limit = 1000000
    
    # 1. Sieve of Eratosthenes (Pre-compute primes)
    # We create a boolean array. is_prime[n] is True if n is prime.
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False # 0 and 1 are not primes
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, limit, i):
                is_prime[j] = False
                
    # Create a set for O(1) fast lookups
    # "set" lookups are much faster than "list" lookups
    primes_set = set(num for num, prime in enumerate(is_prime) if prime)

    # 2. Check for Circular Primes
    circular_primes_count = 0
    
    for num in primes_set:
        s_num = str(num)
        all_rotations_prime = True
        
        # Generate all rotations
        # Example for 197: range(3) -> i=0, 1, 2
        # i=1: s_num[1:] + s_num[:1] -> "97" + "1" = "971"
        for i in range(1, len(s_num)):
            rotated_str = s_num[i:] + s_num[:i]
            rotated_num = int(rotated_str)
            
            if rotated_num not in primes_set:
                all_rotations_prime = False
                break
        
        if all_rotations_prime:
            circular_primes_count += 1

    print(f"Limit: {limit}")
    print(f"Number of circular primes found: {circular_primes_count}")

if __name__ == "__main__":
    solve_circular_primes()