"""
Project Euler Problem 20: Factorial Digit Sum

n! means n * (n-1) * ... * 3 * 2 * 1

For example, 10! = 3,628,800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math

def solve_factorial_digit_sum():
    # 1. Calculate 100! (100 factorial)
    # math.factorial(n) computes the product of all integers from 1 to n.
    # Python handles the massive result automatically.
    number = math.factorial(100)
    
    # Optional: Print the number just to see how big it is
    # print(f"100! is: {number}")
    
    # 2. Convert the number to a string
    # This allows us to treat each digit as a character.
    number_str = str(number)
    
    # 3. Sum the digits
    # Iterate through each character 'd', convert it back to int, and sum them.
    digit_sum = sum(int(d) for d in number_str)
    
    print(f"The calculated factorial starts with: {number_str[:10]}...")
    print(f"The total number of digits is: {len(number_str)}")
    print("-" * 30)
    print(f"The sum of the digits is: {digit_sum}")

if __name__ == "__main__":
    solve_factorial_digit_sum()