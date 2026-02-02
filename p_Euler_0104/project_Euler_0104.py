"""
Project Euler Problem 104: Pandigital Fibonacci Ends

Find the first Fibonacci number for which the first nine digits 
AND the last nine digits are 1-9 pandigital.
"""

import math

def is_pandigital(n):
    """
    Checks if a number (or string of digits) contains digits 1-9 exactly once.
    Note: The problem specifies 1-9 pandigital, so 0 is not allowed.
    """
    s = str(n)
    if len(s) != 9:
        return False
    return set(s) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

def solve_pandigital_fibonacci():
    # Constants for Binet's formula approximation
    # Fn ~ phi^n / sqrt(5)
    # log10(Fn) ~ n*log10(phi) - 0.5*log10(5)
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    log_phi = math.log10(phi)
    log_sqrt_5 = math.log10(sqrt_5)
    
    # Modular arithmetic for the TAIL (last 9 digits)
    # We iterate calculating F_k % 10^9
    f1 = 1
    f2 = 1
    mod = 10**9
    
    k = 2 # Current index (we start loop at k=3)
    
    print("Searching for pandigital Fibonacci ends...")
    
    while True:
        k += 1
        
        # Calculate next Fibonacci number modulo 10^9
        # f3 = f1 + f2
        f3 = (f1 + f2) % mod
        
        # Shift
        f1 = f2
        f2 = f3
        
        # Optimization: Only check head if tail is pandigital
        # This check is fast integer arithmetic
        if is_pandigital(f3):
            
            # Now calculate the HEAD (first 9 digits) using Logarithms
            # We need high precision, standard float is usually enough for 9 digits
            
            # log_val = log10(F_k)
            log_val = k * log_phi - log_sqrt_5
            
            # We want the first 9 digits.
            # The fractional part determines the digits: 10^(fractional_part)
            fractional_part = log_val - int(log_val)
            
            # 10^fractional_part gives 1.xxxxxx
            # Multiply by 10^8 to get 9 digits integer
            head_approx = int(pow(10, fractional_part + 8))
            
            if is_pandigital(head_approx):
                print("-" * 30)
                print(f"Solution found at k = {k}")
                print(f"Tail: {f3}")
                print(f"Head: {head_approx}")
                break

if __name__ == "__main__":
    solve_pandigital_fibonacci()