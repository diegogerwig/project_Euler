"""
Project Euler Problem 34: Digit Factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

def solve_digit_factorials():
    # 1. Precompute factorials for digits 0-9
    # This is much faster than calculating math.factorial() every time inside the loop.
    # 0! = 1, 1! = 1, 2! = 2, ..., 9! = 362880
    factorials = [1] * 10
    current_fact = 1
    for i in range(1, 10):
        current_fact *= i
        factorials[i] = current_fact
        
    # factorials list is now: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    # 2. Define the upper limit
    # The maximum value for a 7-digit number is 9,999,999.
    # The maximum sum of factorials for 7 digits is 7 * 9! = 2,540,160.
    # An 8-digit number implies a minimum value of 10,000,000, which is > 2,540,160.
    # So we only need to search up to ~2.5 million.
    limit = 2540161
    
    total_sum = 0
    found_numbers = []
    
    # 3. Iterate and Check
    # We start from 3 because 1 and 2 are excluded by the problem description.
    for n in range(3, limit):
        
        # Calculate sum of factorials of digits
        # We convert number to string to iterate over digits easily
        digit_sum = 0
        for char in str(n):
            digit_val = int(char)
            digit_sum += factorials[digit_val]
            
            # Optimization: If partial sum already exceeds n, we can stop early
            if digit_sum > n:
                break
        
        # Check if it matches
        if digit_sum == n:
            found_numbers.append(n)
            total_sum += n

    print(f"Curious numbers found: {found_numbers}")
    print(f"Total sum: {total_sum}")

if __name__ == "__main__":
    solve_digit_factorials()