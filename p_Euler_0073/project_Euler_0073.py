"""
Project Euler Problem 73: Counting Fractions in a Range

How many fractions lie between 1/3 and 1/2 in the sorted set of 
reduced proper fractions for d <= 12,000?
"""

import math

def solve_counting_fractions():
    limit = 12000
    count = 0
    
    # We iterate through all possible denominators
    # We start at 4 because for d=2,3 no fraction fits strictly between 1/3 and 1/2.
    for d in range(4, limit + 1):
        
        # Calculate the bounds for the numerator n
        # n > d/3  =>  n >= floor(d/3) + 1
        # n < d/2  =>  n <= ceiling(d/2) - 1  => which is equivalent to floor((d-1)/2)
        
        lower_bound = d // 3 + 1
        upper_bound = (d - 1) // 2
        
        for n in range(lower_bound, upper_bound + 1):
            # Check if it is a reduced fraction
            if math.gcd(n, d) == 1:
                count += 1
                
    print(f"Number of reduced fractions between 1/3 and 1/2: {count}")

if __name__ == "__main__":
    solve_counting_fractions()