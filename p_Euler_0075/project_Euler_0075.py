"""
Project Euler Problem 75: Singular Integer Right Triangles

Given that L is the length of the wire, for how many values of L <= 1,500,000
can exactly one integer sided right angle triangle be formed?

Method: Generate Pythagorean triples using Euclid's formula.
L = 2m(m+n)
"""

import math

def solve_singular_integer_right_triangles():
    limit = 1500000
    # counts[i] stores the number of ways a wire of length i can form a right triangle
    counts = [0] * (limit + 1)
    
    # m_limit: 2m^2 < limit => m < sqrt(limit/2)
    m_limit = int((limit / 2) ** 0.5)
    
    for m in range(2, m_limit + 1):
        for n in range(1, m):
            # Conditions for primitive triple:
            # 1. (m - n) is odd (opposite parity)
            # 2. gcd(m, n) == 1 (coprime)
            if (m + n) % 2 == 1 and math.gcd(m, n) == 1:
                
                # Perimeter of the primitive triangle
                p = 2 * m * (m + n)
                
                if p > limit:
                    break
                
                # Mark p and all its multiples
                # k*p represents non-primitive triples derived from this primitive one
                for k in range(p, limit + 1, p):
                    counts[k] += 1
                    
    # Count how many lengths have exactly one solution
    result = counts.count(1)
    
    print(f"Number of values of L <= {limit} with exactly one solution: {result}")

if __name__ == "__main__":
    solve_singular_integer_right_triangles()