"""
Project Euler Problem 125: Palindromic Sums

Find the sum of all numbers less than 10^8 that are both palindromic 
and can be written as the sum of consecutive squares.
"""

def solve_palindromic_sums():
    limit = 10**8
    # We iterate up to sqrt(limit) because i^2 must be less than limit.
    # Actually, strictly speaking, 2*i^2 < limit, but sqrt(limit) is a safe upper bound.
    sqrt_limit = int(limit**0.5) + 1
    
    # Use a set to store found numbers to avoid duplicates
    # (A number might be the sum of consecutive squares in more than one way)
    valid_numbers = set()
    
    # Outer loop: The starting number of the sequence (i)
    for i in range(1, sqrt_limit):
        current_sum = i * i
        
        # Inner loop: Add subsequent squares (i+1, i+2, ...)
        for j in range(i + 1, sqrt_limit):
            current_sum += j * j
            
            if current_sum >= limit:
                break
            
            # Check if palindrome
            s = str(current_sum)
            if s == s[::-1]:
                valid_numbers.add(current_sum)
                # Optional debug to see what we found
                # print(f"Found {current_sum} (from {i}^2 to {j}^2)")

    total_sum = sum(valid_numbers)
    
    print(f"Sum of all valid numbers less than {limit}: {total_sum}")

if __name__ == "__main__":
    solve_palindromic_sums()