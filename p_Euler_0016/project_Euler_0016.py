"""
Project Euler Problem 16: Power Digit Sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def solve_power_digit_sum():
    """
    Calculates the sum of the digits of 2 to the power of 1000.
    
    Python handles arbitrarily large integers natively, so we can 
    compute 2**1000 directly without worrying about integer overflow.
    """
    
    # 1. Calculate the massive number
    # 2**1000 creates a number with approximately 302 digits.
    number = 2 ** 1000
    
    # 2. Convert the number to a string to iterate over digits
    number_str = str(number)
    
    # 3. Iterate through characters, convert back to int, and sum them
    # Using a generator expression for memory efficiency
    digit_sum = sum(int(digit) for digit in number_str)
    
    print(f"2^1000 is a number with {len(number_str)} digits.")
    print(f"The sum of its digits is: {digit_sum}")

if __name__ == "__main__":
    solve_power_digit_sum()