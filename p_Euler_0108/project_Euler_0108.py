"""
Project Euler Problem 108: Diophantine Reciprocals I

Find the least value of n for which the number of distinct solutions 
to 1/x + 1/y = 1/n exceeds 1000.

Logic:
Solutions = (d(n^2) + 1) / 2 > 1000
d(n^2) > 1999
n = p1^a1 * p2^a2 ...
d(n^2) = (2*a1 + 1) * (2*a2 + 1) ...
"""

import sys

def solve_diophantine_reciprocals():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    limit_divisors = 1999
    best_n = float('inf')
    
    def search(index, current_n, current_divs):
        nonlocal best_n
        
        # Pruning: if current_n is already worse than best found, stop
        if current_n >= best_n:
            return
            
        # Check if we met the condition
        if current_divs > limit_divisors:
            best_n = current_n
            return
            
        # Iterate exponents for the current prime
        # We enforce decreasing exponents: a_i <= a_{i-1}
        # For the first prime (index 0), limit is arbitrary but ~20 covers it
        # (2^20 is > 1 million, sufficient for this problem)
        
        limit_exponent = 20 
        
        # If not the first prime, capped by the previous exponent used (passed via args if needed, 
        # but here we can just loop down and let the logic flow naturally, 
        # though strictly ensuring a_i <= a_{i-1} optimizes search).
        # For simplicity in this small problem, we iterate normally but stop if n gets too big.
        
        p = primes[index]
        
        # Try exponents from 1 upwards
        # Optimization: We accumulate n. If n exceeds best_n, loop breaks.
        exponent = 1
        while True:
            # Calculate contribution to n and divisors
            # We are multiplying current_n by p repeatedly
            next_n = current_n * (p ** exponent)
            
            # Divisors update: 
            # We replace the factor 1 (implicit) with (2*exponent + 1)
            # Actually, the recursive step should multiply current_divs by the new term.
            next_divs = current_divs * (2 * exponent + 1)
            
            if next_n >= best_n:
                break
            
            # Recurse to next prime
            search(index + 1, next_n, next_divs)
            
            exponent += 1
            
    # Start search: index 0, current_n = 1, current_divisors = 1
    search(0, 1, 1)
    
    print(f"Least value of n: {best_n}")
    
    # Verification
    n_squared_divs = 1
    temp_n = best_n
    for p in primes:
        if temp_n % p == 0:
            count = 0
            while temp_n % p == 0:
                count += 1
                temp_n //= p
            n_squared_divs *= (2 * count + 1)
            
    solutions = (n_squared_divs + 1) // 2
    print(f"Number of distinct solutions: {solutions}")

if __name__ == "__main__":
    solve_diophantine_reciprocals()