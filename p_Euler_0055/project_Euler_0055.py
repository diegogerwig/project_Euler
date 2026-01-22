"""
Project Euler Problem 55: Lychrel Numbers

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
A number that never forms a palindrome through the reverse and add process (within 50 iterations)
is called a Lychrel number.

How many Lychrel numbers are there below ten-thousand?
"""

def is_palindrome(n):
    """Checks if a number reads the same forwards and backwards."""
    s = str(n)
    return s == s[::-1]

def is_lychrel(n):
    """
    Returns True if n is a Lychrel number (does not form a palindrome in 50 iterations).
    Returns False otherwise.
    """
    current_val = n
    
    for _ in range(50):
        # Reverse and add
        reversed_val = int(str(current_val)[::-1])
        current_val += reversed_val
        
        # Check if the RESULT is a palindrome
        if is_palindrome(current_val):
            return False
            
    # If we finish the loop without returning False, it's a Lychrel candidate
    return True

def solve_lychrel_numbers():
    lychrel_count = 0
    
    # Check numbers below 10,000 (1 to 9999)
    for i in range(1, 10000):
        if is_lychrel(i):
            lychrel_count += 1
            
    print(f"Total Lychrel numbers below 10,000: {lychrel_count}")

if __name__ == "__main__":
    solve_lychrel_numbers()