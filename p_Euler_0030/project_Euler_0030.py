"""
Project Euler Problem 30: Digit Fifth Powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
Note: 1 = 1^5 is not included.
"""

def solve_digit_fifth_powers():
    # 1. Precompute the 5th powers for digits 0-9
    # This avoids calculating power operations inside the main loop (optimization)
    powers = [i ** 5 for i in range(10)]
    
    # 2. Define the upper limit
    # Max sum for a 6-digit number is 6 * 9^5 = 354,294.
    # A 7-digit number creates a sum that is too small to match the number itself.
    limit = 355000
    
    total_sum = 0
    found_numbers = []
    
    # 3. Iterate from 2 to limit (1 is excluded by problem statement)
    for num in range(2, limit):
        
        # Calculate sum of 5th powers of digits
        # Converting to string is an easy way to iterate over digits
        current_sum = sum(powers[int(digit)] for digit in str(num))
        
        if current_sum == num:
            found_numbers.append(num)
            total_sum += num
            
    print(f"Numbers found: {found_numbers}")
    print(f"Total sum: {total_sum}")

if __name__ == "__main__":
    solve_digit_fifth_powers()