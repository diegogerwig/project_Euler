"""
Project Euler Problem 58: Spiral Primes

Starting with 1 and spiralling anticlockwise.
Find the side length of the square spiral for which the ratio of primes 
along both diagonals first falls below 10%.
"""

def is_prime(n):
    """Efficient primality check."""
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    # Check odd divisors up to sqrt(n)
    # Since n grows large, this is the bottleneck.
    # Miller-Rabin would be faster for huge numbers, but for n ~ 26000 
    # trial division is still very fast (sqrt is small).
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def solve_spiral_primes():
    # Start with the center
    # Side length starts at 1, but loop starts logic at layer 1 (side 3)
    side_length = 1
    prime_count = 0
    total_nums = 1  # The center '1'
    
    while True:
        side_length += 2
        
        # The four corners for current side_length n are:
        # n^2
        # n^2 - (n-1)
        # n^2 - 2(n-1)
        # n^2 - 3(n-1)
        
        sq = side_length * side_length
        step = side_length - 1
        
        c1 = sq           # Bottom-Right (Never prime for n > 1)
        c2 = sq - step    # Bottom-Left
        c3 = sq - 2*step  # Top-Left
        c4 = sq - 3*step  # Top-Right
        
        # We check primality for the 3 candidates
        if is_prime(c2): prime_count += 1
        if is_prime(c3): prime_count += 1
        if is_prime(c4): prime_count += 1
        
        # Update total numbers on diagonals
        # We add 4 corners every layer
        total_nums += 4
        
        # Calculate ratio
        ratio = prime_count / total_nums
        
        if ratio < 0.10:
            print(f"Ratio fell below 10% at side length: {side_length}")
            print(f"Primes: {prime_count}, Total: {total_nums}, Ratio: {ratio:.4f}")
            break

if __name__ == "__main__":
    solve_spiral_primes()