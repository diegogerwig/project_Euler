"""
Project Euler Problem 112: Bouncy Numbers

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

def is_bouncy(n):
    """
    Returns True if n is a bouncy number (neither increasing nor decreasing).
    """
    # Numbers below 100 cannot be bouncy (e.g., 89 is increasing, 98 decreasing)
    if n < 100:
        return False
        
    s = str(n)
    
    # Check if increasing: sorted(s) == list(s)
    # Check if decreasing: sorted(s, reverse=True) == list(s)
    
    # While sorting is O(D log D), for small number of digits (D < 10) it's very fast.
    # We can use a flag based approach for pure speed, but this is readable.
    
    s_list = list(s)
    sorted_s = sorted(s_list)
    
    if s_list == sorted_s:
        return False # It is increasing
        
    if s_list == sorted_s[::-1]:
        return False # It is decreasing
        
    return True

def solve_bouncy_numbers():
    bouncy_count = 0
    n = 99 # We know numbers below 100 aren't bouncy
    
    # We are looking for 99%
    target_percentage = 99
    
    while True:
        n += 1
        
        if is_bouncy(n):
            bouncy_count += 1
            
        # Check proportion
        # bouncy / n == 99 / 100
        # => 100 * bouncy == 99 * n
        if 100 * bouncy_count == target_percentage * n:
            print(f"Target reached at n: {n}")
            print(f"Bouncy count: {bouncy_count}")
            print(f"Proportion: {bouncy_count/n:.2%}")
            break

if __name__ == "__main__":
    solve_bouncy_numbers()