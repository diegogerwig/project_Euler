"""
Project Euler Problem 64: Odd Period Square Roots

How many continued fractions for N <= 10000 have an odd period?

Algorithm:
m_{k+1} = d_k * a_k - m_k
d_{k+1} = (N - m_{k+1}^2) / d_k
a_{k+1} = floor((a_0 + m_{k+1}) / d_{k+1})
Stop when a_k == 2 * a_0
"""

import math

def get_period_length(n):
    # Integer part of sqrt(n)
    a0 = math.isqrt(n)
    
    # If perfect square, period is 0 (no continued fraction expansion)
    if a0 * a0 == n:
        return 0
    
    m = 0
    d = 1
    a = a0
    
    period = 0
    
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        
        period += 1
        
        # The specific property of sqrt expansions is that the cycle ends
        # when the coefficient 'a' becomes twice the integer part of the root.
        if a == 2 * a0:
            break
            
    return period

def solve_odd_period_roots():
    limit = 10000
    odd_period_count = 0
    
    print(f"Checking numbers up to {limit}...")
    
    for n in range(1, limit + 1):
        length = get_period_length(n)
        
        if length % 2 != 0:
            odd_period_count += 1
            
    print(f"Total numbers with odd period: {odd_period_count}")

if __name__ == "__main__":
    solve_odd_period_roots()