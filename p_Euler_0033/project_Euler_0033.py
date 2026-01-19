"""
Project Euler Problem 33: Digit Cancelling Fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, 
is obtained by cancelling the 9s.

Find the denominator of the product of the four non-trivial examples.
"""

import math

def solve_digit_cancelling():
    product_numerator = 1
    product_denominator = 1
    
    found_fractions = []

    # 1. Loop through denominators and numerators
    for d in range(11, 100):
        for n in range(10, d): # n < d because value is less than 1
            
            # Skip trivial examples (multiples of 10)
            if n % 10 == 0 and d % 10 == 0:
                continue
            
            # 2. Convert to strings to find common digits
            s_n = str(n)
            s_d = str(d)
            
            # Find the intersection (common digits)
            common = set(s_n) & set(s_d)
            
            if not common:
                continue
                
            # 3. Check the "bad" simplification
            for digit in common:
                # Remove the digit from both numerator and denominator
                # We interpret them as lists to remove specific instances easily
                list_n = list(s_n)
                list_d = list(s_d)
                
                list_n.remove(digit)
                list_d.remove(digit)
                
                # If denominator becomes 0 after removal (shouldn't happen with our filters, but safety first)
                if list_d[0] == '0':
                    continue
                
                new_n = int(list_n[0])
                new_d = int(list_d[0])
                
                if new_d == 0:
                    continue
                
                # 4. Compare Values
                # Check if n/d == new_n/new_d
                # Cross multiplication is safer than float comparison: n * new_d == d * new_n
                if n * new_d == d * new_n:
                    found_fractions.append(f"{n}/{d}")
                    
                    # Accumulate the product
                    product_numerator *= new_n
                    product_denominator *= new_d
                    
                    # Break to avoid double counting if a number has two same digits
                    break
    
    # 5. Simplify the final fraction
    # We need the fraction in its lowest common terms.
    # We calculate the Greatest Common Divisor (GCD).
    common_divisor = math.gcd(product_numerator, product_denominator)
    
    final_denominator = product_denominator // common_divisor
    
    print("Fractions found:", found_fractions)
    print(f"Product (unsimplified): {product_numerator}/{product_denominator}")
    print(f"Simplified denominator: {final_denominator}")

if __name__ == "__main__":
    solve_digit_cancelling()