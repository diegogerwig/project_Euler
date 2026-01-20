"""
Project Euler Problem 52: Permuted Multiples

It can be seen that the number, 125874, and its double, 251748, contain 
exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
"""

def solve_permuted_multiples():
    # We start searching from 1. 
    # Realistically, we could skip numbers that don't start with 1,
    # but Python is fast enough to brute force this sequentially.
    x = 1
    
    while True:
        # Get the sorted digits of x as a signature
        # e.g., 125874 -> ['1', '2', '4', '5', '7', '8']
        digits_x = sorted(str(x))
        
        # We assume it's valid until proven otherwise
        found = True
        
        # Check multipliers 2 through 6
        for multiplier in range(2, 7):
            current_val = x * multiplier
            
            # If sorted digits don't match, this x is invalid. Break inner loop.
            if sorted(str(current_val)) != digits_x:
                found = False
                break
        
        # If the loop finished and 'found' is still True, we have our number
        if found:
            print(f"Found the number: {x}")
            print(f"2x: {2*x}")
            print(f"3x: {3*x}")
            print(f"4x: {4*x}")
            print(f"5x: {5*x}")
            print(f"6x: {6*x}")
            break
            
        x += 1

if __name__ == "__main__":
    solve_permuted_multiples()