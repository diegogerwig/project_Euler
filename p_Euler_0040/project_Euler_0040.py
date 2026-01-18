"""
Project Euler Problem 40: Champernowne's Constant

An irrational decimal fraction is created by concatenating the positive integers:
0.12345678910111213141516...

Find the value of the expression:
d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
"""

def solve_champernowne():
    # 1. Construct the decimal part string
    # We need to reach the 1,000,000th digit.
    # Let's estimate how many numbers we need to concatenate.
    # 1-digit numbers (1-9): 9 digits
    # 2-digit numbers (10-99): 180 digits
    # ...
    # 5-digit numbers: ~450,000 digits
    # 6-digit numbers: will easily take us over 1,000,000 digits.
    # So iterating up to 200,000 integers is more than enough.
    
    # We join numbers starting from 1.
    champernowne_str = "".join(str(i) for i in range(1, 250000))
    
    # 2. Define the target indices
    # The problem uses 1-based indexing (d1 is the 1st digit).
    # Python uses 0-based indexing. So d1 is at index 0, d10 is at index 9.
    targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
    
    product = 1
    
    print("Digits found:")
    
    # 3. Extract and multiply
    for t in targets:
        # Adjust for 0-based index
        index = t - 1
        
        digit_char = champernowne_str[index]
        digit = int(digit_char)
        
        print(f"d_{t}: {digit}")
        
        product *= digit

    print("-" * 20)
    print(f"Final Product: {product}")

if __name__ == "__main__":
    solve_champernowne()