"""
Project Euler Problem 57: Square Root Convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

def solve_square_root_convergents():
    # Start with the first expansion: 3/2
    n = 3
    d = 2
    
    count = 0
    
    # We need to check the first 1000 expansions.
    # We already have the 1st one (3/2) in variables, but we check inside loop.
    # Or cleaner: loop 1000 times, check, then update.
    
    for _ in range(1000):
        # 1. Check condition (numerator digits > denominator digits)
        # Converting to string is the easiest way to count digits in Python
        if len(str(n)) > len(str(d)):
            count += 1
            
        # 2. Update values for next iteration using the recurrence relation
        # We use a temporary variable or tuple unpacking to update simultaneously
        # n_new = n + 2*d
        # d_new = n + d
        n, d = n + 2*d, n + d
        
    print(f"Fractions with more digits in numerator: {count}")

if __name__ == "__main__":
    solve_square_root_convergents()