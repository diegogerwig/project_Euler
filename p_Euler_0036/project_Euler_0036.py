"""
Project Euler Problem 36: Double-base Palindromes

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""

def solve_double_base_palindromes():
    limit = 1000000
    total_sum = 0
    
    # 1. Iterate through numbers
    # Optimization: We start at 1 and use a step of 2 (1, 3, 5...)
    # Even numbers end in 0 in binary. Since leading zeros aren't allowed,
    # a binary number must start with 1, so it must end with 1 to be a palindrome.
    for n in range(1, limit, 2):
        
        # 2. Check Base 10 Palindrome
        s_decimal = str(n)
        if s_decimal == s_decimal[::-1]:
            
            # 3. Check Base 2 Palindrome
            # bin(n) returns something like '0b1001001'
            # [2:] slices off the '0b' prefix
            s_binary = bin(n)[2:]
            
            if s_binary == s_binary[::-1]:
                total_sum += n
                # Optional: Print found numbers to see progress
                # print(f"Found: {n} (Decimal) -> {s_binary} (Binary)")

    print(f"Sum of all double-base palindromes under {limit}: {total_sum}")

if __name__ == "__main__":
    solve_double_base_palindromes()