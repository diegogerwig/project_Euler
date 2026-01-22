"""
Project Euler Problem 56: Powerful Digit Sum

A googol (10^100) is a massive number: one followed by one-hundred zeros.
Considering natural numbers of the form, a^b, where a, b < 100, 
what is the maximum digital sum?
"""

def solve_powerful_digit_sum():
    max_digit_sum = 0
    
    # Iterate a and b from 1 to 99 (since a, b < 100)
    # We could optimize by skipping small numbers (e.g. start at 50),
    # but 100x100 iterations is instantaneous for a computer.
    for a in range(1, 100):
        for b in range(1, 100):
            
            # Python handles large integers automatically
            power = a ** b
            
            # Convert to string and sum digits
            # Example: sum(int(d) for d in "123") -> 1+2+3 = 6
            digit_sum = sum(int(d) for d in str(power))
            
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
                # Optional: print the 'record breakers' to see progress
                # print(f"New max: {max_digit_sum} (from {a}^{b})")

    print(f"Maximum digital sum found: {max_digit_sum}")

if __name__ == "__main__":
    solve_powerful_digit_sum()