"""
Project Euler Problem 27: Quadratic Primes

Find the product of the coefficients, a and b, for the quadratic expression 
n^2 + an + b that produces the maximum number of primes for consecutive 
values of n, starting with n = 0.

Constraints: |a| < 1000, |b| <= 1000
"""

def is_prime(num):
    """
    Checks if a number is prime.
    We handle negatives and small numbers because the formula might produce them.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(num)
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def solve_quadratic_primes():
    # 1. Generate primes for 'b' candidates
    # Since n=0 gives 'b', b must be a prime number.
    # We look for primes up to 1000.
    b_candidates = []
    for i in range(2, 1001):
        if is_prime(i):
            b_candidates.append(i)
            
    best_n = 0
    best_a = 0
    best_b = 0
    
    # 2. Iterate through coefficients
    # 'a' is between -999 and 999 (since |a| < 1000)
    for a in range(-999, 1000):
        
        # 'b' must be a prime number (positive, because n=0 -> prime)
        # Note: The problem says |b| <= 1000, but negatives yield negative primes for n=0?
        # Actually primes are defined as positive integers > 1. 
        # So b must be positive prime.
        for b in b_candidates:
            
            n = 0
            while True:
                # Calculate the quadratic value
                value = (n * n) + (a * n) + b
                
                # Check if it produces a prime
                if is_prime(value):
                    n += 1
                else:
                    # Sequence broken
                    break
            
            # 3. Update maximum if this chain is longer
            if n > best_n:
                best_n = n
                best_a = a
                best_b = b
                
    product = best_a * best_b
    
    print(f"Longest sequence found: {best_n} consecutive primes")
    print(f"Coefficients: a = {best_a}, b = {best_b}")
    print(f"Product a * b = {product}")

if __name__ == "__main__":
    solve_quadratic_primes()