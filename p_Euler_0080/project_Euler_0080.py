"""
Project Euler Problem 80: Square Root Digital Expansion

Calculate the digital sum of the first 100 decimal digits for all 
irrational square roots of numbers from 1 to 100.
"""

import math

def solve_square_root_digital_expansion():
    total_digital_sum = 0
    limit = 100
    precision_digits = 100
    
    # We need to shift by 10^(2*100) to get 100 digits of precision.
    # Actually, root(N * 10^200) gives approx 101 digits for N >= 1.
    # We slice the first 100.
    multiplier = 10 ** (2 * precision_digits)
    
    for n in range(1, limit + 1):
        # 1. Check if perfect square
        sqrt_n = math.isqrt(n)
        if sqrt_n * sqrt_n == n:
            continue
            
        # 2. Calculate high precision root using integer arithmetic
        # We compute integer_sqrt(n * 10^200)
        # Python handles arbitrarily large integers automatically.
        huge_number = n * multiplier
        root = math.isqrt(huge_number)
        
        # 3. Get the first 100 digits
        root_str = str(root)
        # Just to be safe, take exactly the first 100 chars
        digits = root_str[:precision_digits]
        
        # 4. Sum the digits
        current_sum = sum(int(d) for d in digits)
        total_digital_sum += current_sum
        
        # Debug print for example n=2
        if n == 2:
            print(f"sqrt(2) digits: {digits}")
            print(f"Sum: {current_sum}")

    print(f"Total of the digital sums: {total_digital_sum}")

if __name__ == "__main__":
    solve_square_root_digital_expansion()