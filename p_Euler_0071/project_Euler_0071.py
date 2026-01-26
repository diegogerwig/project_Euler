"""
Project Euler Problem 71: Ordered Fractions

Find the numerator of the fraction immediately to the left of 3/7
for denominators <= 1,000,000.
"""

def solve_ordered_fractions():
    target_n = 3
    target_d = 7
    limit = 1000000
    
    # We want to maximize n/d such that n/d < 3/7
    
    best_n = 0
    best_d = 1
    
    # We iterate denominators from limit down to 2.
    # Logic suggests the best answer will have a large denominator.
    for d in range(limit, 2, -1):
        
        # Calculate the closest n strictly less than (3/7) * d
        # n < (3 * d) / 7
        # Since integer division // floors the result:
        # If (3*d) % 7 == 0, then (3*d)//7 gives the exact value equal to 3/7.
        # We need strict inequality, so we subtract 1 in that case.
        # Otherwise, floor is exactly what we want.
        
        if (target_n * d) % target_d == 0:
            n = (target_n * d) // target_d - 1
        else:
            n = (target_n * d) // target_d
            
        # Compare current fraction n/d with best_n/best_d
        # To avoid floating point issues, we use cross-multiplication:
        # n/d > best_n/best_d  <=>  n * best_d > best_n * d
        
        if n * best_d > best_n * d:
            best_n = n
            best_d = d
            # Optimization: If we find a very close match with a large denominator,
            # it's hard to beat. We could theoretically break early with some math bounds,
            # but 1M iterations is fast enough.
            
    print(f"The fraction immediately to the left of 3/7 is {best_n}/{best_d}")
    print(f"Numerator: {best_n}")

if __name__ == "__main__":
    solve_ordered_fractions()