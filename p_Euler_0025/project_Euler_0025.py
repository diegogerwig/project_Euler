"""
Project Euler Problem 25: 1000-digit Fibonacci Number

The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def solve_fibonacci_digits():
    # 1. Initialize variables
    # We start with the first two terms
    fn_prev = 1  # F1
    fn_curr = 1  # F2
    index = 2    # We are currently at the 2nd term
    
    # 2. Iterate until we find the number
    # len(str(n)) converts the number to text to count the characters (digits)
    while len(str(fn_curr)) < 1000:
        
        # Calculate the next Fibonacci number
        # Old current becomes the new previous
        # New current becomes sum of old current + old previous
        fn_prev, fn_curr = fn_curr, fn_prev + fn_curr
        
        # Increment the index counter
        index += 1
        
    # 3. Print the result
    print(f"The first term with 1000 digits is at index: {index}")
    print(f"The number is: {str(fn_curr)}")

if __name__ == "__main__":
    solve_fibonacci_digits()