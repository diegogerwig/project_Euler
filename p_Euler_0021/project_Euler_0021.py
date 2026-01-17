"""
Project Euler Problem 21: Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n.
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math

def get_sum_of_divisors(n):
    """
    Calculates the sum of proper divisors of n.
    Example: divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110.
    Sum = 284.
    """
    if n <= 1:
        return 0
    
    total_sum = 1  # 1 is always a proper divisor for n > 1
    
    # We only need to loop up to the square root of n to find divisors pairs
    limit = int(math.sqrt(n))
    
    for i in range(2, limit + 1):
        if n % i == 0:
            total_sum += i
            
            # If the divisors are distinct (not a perfect square root), add the pair
            # e.g., for 10: i=2, adds 2. Also adds 10/2 = 5.
            if i != (n // i):
                total_sum += (n // i)
                
    return total_sum

def solve_amicable_numbers():
    amicable_numbers = set()
    limit = 10000
    
    # Iterate through all numbers under the limit
    for a in range(2, limit):
        
        # Calculate b = d(a)
        b = get_sum_of_divisors(a)
        
        # Optimization: 
        # 1. b must be different from a (condition a != b)
        # 2. b must be > 1 to be a valid candidate
        # 3. We can check if b < limit to keep within bounds (though not strictly required by problem logic, usually implies pairs within range)
        if b != a and b > 1:
            
            # Calculate d(b)
            db = get_sum_of_divisors(b)
            
            # Check the Amicable condition: d(b) = a
            if db == a:
                amicable_numbers.add(a)
                # We could add 'b' here too, but the loop will reach 'b' eventually.
                # Adding just 'a' ensures we don't double count if we iterate fully.
    
    total_sum = sum(amicable_numbers)
    
    print(f"Amicable numbers found: {sorted(list(amicable_numbers))}")
    print(f"Sum of all amicable numbers under {limit}: {total_sum}")

if __name__ == "__main__":
    solve_amicable_numbers()