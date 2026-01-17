"""
Project Euler Problem 48: Self Powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def solve_self_powers():
    limit = 1000
    
    # We only care about the last 10 digits.
    # This is our modulus (10^10).
    modulo = 10000000000
    
    total_sum = 0
    
    for i in range(1, limit + 1):
        # Python's built-in pow(base, exp, mod) is extremely efficient.
        # It calculates (i ** i) % modulo without ever creating the huge number.
        term = pow(i, i, modulo)
        
        total_sum += term
        
    # Take the modulo of the final sum just in case the sum itself exceeded 10 digits
    result = total_sum % modulo
    
    print(f"The last 10 digits are: {result}")

    # --- ALTERNATIVE ONE-LINER (Brute Force) ---
    # Python is so powerful that it can actually calculate the full number 
    # and slice the string in a fraction of a second.
    # 
    # print(str(sum(i**i for i in range(1, 1001)))[-10:])

if __name__ == "__main__":
    solve_self_powers()