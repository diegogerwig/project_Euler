"""
Project Euler Problem 47: Distinct Primes Factors

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""

def solve_distinct_primes_factors():
    # We need to find 4 consecutive numbers.
    # We estimate the limit. 2*3*5*7 = 210 is the smallest number with 4 factors.
    # The sequence is likely in the 100,000 range.
    limit = 200000
    
    # factors_count[i] stores the number of distinct prime factors of i
    factors_count = [0] * limit
    
    # 1. Populate the sieve
    for i in range(2, limit):
        # If factors_count[i] is 0, it means i is prime (we haven't touched it yet)
        if factors_count[i] == 0:
            # Add 1 to the count of distinct factors for all multiples of this prime
            for j in range(i, limit, i):
                factors_count[j] += 1
                
    # 2. Find the consecutive sequence
    consecutive_goal = 4
    current_run = 0
    
    for i in range(2, limit):
        if factors_count[i] == consecutive_goal:
            current_run += 1
        else:
            current_run = 0
            
        if current_run == consecutive_goal:
            # Found it! 'i' is the last number in the sequence
            # The first number is i - 3
            first_number = i - 3
            print(f"Sequence found:")
            print(f"{first_number} (Factors: {factors_count[first_number]})")
            print(f"{first_number+1} (Factors: {factors_count[first_number+1]})")
            print(f"{first_number+2} (Factors: {factors_count[first_number+2]})")
            print(f"{first_number+3} (Factors: {factors_count[first_number+3]})")
            print(f"The first of these numbers is: {first_number}")
            return

if __name__ == "__main__":
    solve_distinct_primes_factors()