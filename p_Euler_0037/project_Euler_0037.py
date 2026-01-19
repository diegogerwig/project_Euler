"""
Project Euler Problem 37: Truncatable Primes

The number 3797 is an interesting number. Being prime itself, it is possible to 
continuously remove digits from left to right, and remain prime at each stage: 
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import math

def is_prime(n):
    """Checks if a number is prime efficiently."""
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    """
    Checks if n is both left-truncatable and right-truncatable.
    """
    s_n = str(n)
    
    # Check Left to Right truncation (remove starting digits)
    # Example: 3797 -> 797 -> 97 -> 7
    for i in range(len(s_n)):
        if not is_prime(int(s_n[i:])):
            return False

    # Check Right to Left truncation (remove ending digits)
    # Example: 3797 -> 379 -> 37 -> 3
    # Note: loop goes until len-1 because s_n[:len] is the full number (already checked)
    # but range(1, len) works perfectly for slicing end off.
    for i in range(1, len(s_n)):
        if not is_prime(int(s_n[:i])):
            return False
            
    return True

def solve_truncatable_primes():
    count = 0
    total_sum = 0
    current_num = 11 # Start at 11 because 2,3,5,7 are excluded
    
    found_primes = []
    
    print("Searching for truncatable primes...")
    
    # We loop until we find exactly 11 numbers
    while count < 11:
        if is_prime(current_num):
            if is_truncatable(current_num):
                count += 1
                total_sum += current_num
                found_primes.append(current_num)
                # Optional: Print as we find them
                # print(f"Found {count}/11: {current_num}")
        
        # Optimization: skip even numbers
        current_num += 2

    print(f"The 11 truncatable primes are: {found_primes}")
    print(f"Sum of these primes: {total_sum}")

if __name__ == "__main__":
    solve_truncatable_primes()