"""
Project Euler Problem 66: Diophantine Equation

Find the value of D <= 1000 in minimal solutions of x^2 - Dy^2 = 1 
for which the largest value of x is obtained.

Method: Continued Fractions of sqrt(D).
"""

import math

def solve_diophantine_equation():
    limit = 1000
    max_x = 0
    result_D = 0
    
    # Iterate D from 2 to 1000
    for D in range(2, limit + 1):
        # Skip perfect squares (no integer solutions for x^2 - Dy^2 = 1)
        sqrt_D = int(math.isqrt(D))
        if sqrt_D * sqrt_D == D:
            continue
            
        # Initial parameters for continued fraction expansion of sqrt(D)
        m = 0
        d = 1
        a = sqrt_D
        
        # Convergents (numerators n and denominators dn)
        # We start with the base cases corresponding to the first term a0
        # n1 represents n_{k-1}, n0 represents n_k (current)
        # Initial convergents: p0 = a0/1, p-1 = 1/0
        
        n1 = 1      # n_{k-1}
        n0 = a      # n_{k} (current x candidate)
        
        den1 = 0    # den_{k-1}
        den0 = 1    # den_{k} (current y candidate)
        
        # We don't actually need to store denominators for the x check, 
        # but they are part of the recurrence if we wanted to verify full equation.
        # Actually, x^2 - D*y^2 = 1 test needs y, or simply x^2 % D check?
        # Direct substitution is safest.
        
        while True:
            # Check if current convergent is the solution
            if n0 * n0 - D * den0 * den0 == 1:
                # Solution found!
                if n0 > max_x:
                    max_x = n0
                    result_D = D
                break
            
            # Generate next term in continued fraction
            m = d * a - m
            d = (D - m * m) // d
            a = (sqrt_D + m) // d
            
            # Update convergents (next numerator and denominator)
            # num_new = a * num_curr + num_prev
            n_next = a * n0 + n1
            den_next = a * den0 + den1
            
            # Shift variables for next iteration
            n1 = n0
            n0 = n_next
            den1 = den0
            den0 = den_next
            
    print(f"The value of D <= {limit} with the largest minimal x is: {result_D}")
    print(f"Largest x value: {max_x}")

if __name__ == "__main__":
    solve_diophantine_equation()