"""
Project Euler Problem 53: Combinatoric Selections

There are exactly ten ways of selecting three from five, 12345:
C(5,3) = 10.

It is not until n = 23, that a value exceeds one-million: C(23,10) = 1144066.
How many, not necessarily distinct, values of C(n,r) for 1 <= n <= 100, 
are greater than one-million?
"""

import math

def solve_combinatoric_selections():
    limit = 1000000
    count = 0
    
    # We iterate n from 23 to 100 (inclusive)
    # Why 23? Because the problem states no value exceeds 1M before n=23.
    for n in range(23, 101):
        
        # Optimization: Due to symmetry C(n,r) == C(n, n-r), 
        # we only need to find the FIRST r that exceeds the limit.
        for r in range(1, n // 2 + 1):
            
            # Use Python's built-in combination function (Python 3.8+)
            val = math.comb(n, r)
            
            if val > limit:
                # If C(n, r) > 1M, then all values from r to (n-r) are also > 1M.
                # Example: n=23, first r=10.
                # The valid range is [10, 11, 12, 13].
                # Count = (23 - 10) - 10 + 1 = 4.
                num_values = (n - r) - r + 1
                count += num_values
                
                # We found the start of the "mountain", so we can stop checking this row
                # and move to the next n.
                break
                
    print(f"Values of C(n,r) > 1,000,000: {count}")

if __name__ == "__main__":
    solve_combinatoric_selections()