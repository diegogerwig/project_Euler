"""
Project Euler Problem 120: Square Remainders

Let r be the remainder when (a-1)^n + (a+1)^n is divided by a^2.
Find sum of r_max for 3 <= a <= 1000.

Math derivation:
(a-1)^n + (a+1)^n (mod a^2)
If n is even: remainder is 2.
If n is odd:  remainder is 2na (mod a^2).

To maximize 2na (mod a^2), we want 2n to be as close to a multiple of 'a' as possible
without going over, effectively maximizing the coefficient of 'a'.
Max remainder is a * (a - 1) if a is odd.
Max remainder is a * (a - 2) if a is even.
"""

def solve_square_remainders():
    total_sum = 0
    
    # Iterate a from 3 to 1000
    for a in range(3, 1001):
        # Calculate r_max directly using the derived logic
        # r_max = 2a * ((a-1) // 2)
        # Why? 
        # We want to maximize 2na < a^2.
        # So we maximize 2n < a. The max integer k such that 2na is roughly a^2 is when 2n approx a.
        # The term is 2na. We can vary n (odd).
        # We can effectively pick n such that 2n % a is maximized.
        # Actually simple formula: r_max = 2 * a * ((a - 1) // 2) works for both even and odd.
        
        r_max = 2 * a * ((a - 1) // 2)
        total_sum += r_max
        
    print(f"Sum of r_max for 3 <= a <= 1000: {total_sum}")

if __name__ == "__main__":
    solve_square_remainders()