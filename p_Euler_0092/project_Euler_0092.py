"""
Project Euler Problem 97: Large Non-Mersenne Prime

Find the last ten digits of the prime number:
28433 * 2^7830457 + 1
"""

def solve_large_non_mersenne_prime():
    # We want the last 10 digits, so our modulus is 10^10
    modulus = 10**10
    
    multiplier = 28433
    exponent = 7830457
    
    # 1. Calculate 2^7830457 % 10^10 efficiently
    # pow(base, exp, mod) is extremely fast (modular exponentiation)
    power_part = pow(2, exponent, modulus)
    
    # 2. Multiply by 28433 and add 1, keeping only last 10 digits
    result = (multiplier * power_part + 1) % modulus
    
    print(f"The last ten digits are: {result}")

if __name__ == "__main__":
    solve_large_non_mersenne_prime()