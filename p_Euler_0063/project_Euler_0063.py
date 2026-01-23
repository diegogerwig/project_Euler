"""
Project Euler Problem 63: Powerful Digit Counts

The 5-digit number, 16807 = 7^5, is also a fifth power.
How many n-digit positive integers exist which are also an nth power?

Math derivation:
10^(n-1) <= x^n < 10^n
Implies x < 10 (so x is 1..9)
"""

def solve_powerful_digit_counts():
    count = 0
    
    print("Checking bases 1 to 9...")
    
    # Base x can only be 1 through 9
    for x in range(1, 10):
        n = 1
        while True:
            # Calculate power
            power_val = x ** n
            
            # Get length of digits
            length = len(str(power_val))
            
            if length == n:
                # It matches!
                count += 1
                # Optional: print to see the numbers
                # print(f"{x}^{n} = {power_val} (Length: {length})")
            elif length < n:
                # Once the length falls behind n, it will never catch up
                # because 10^(n-1) grows faster than x^n for x < 10.
                break
            
            n += 1
            
    print(f"Total n-digit positive integers which are also an nth power: {count}")

if __name__ == "__main__":
    solve_powerful_digit_counts()