"""
Project Euler Problem 89: Roman Numerals

Find the number of characters saved by writing each of the 1000 numbers 
in the file in their minimal form.
"""

import urllib.request
import os

def solve_roman_numerals():
    # 1. Download/Read the file
    filename = 'p089_roman.txt'
    url = 'https://projecteuler.net/project/resources/p089_roman.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    # Mappings
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Pairs for minimal generation (Ordered descending)
    val_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def roman_to_int(s):
        """Converts Roman string to Integer."""
        total = 0
        n = len(s)
        for i in range(n):
            val = roman_map[s[i]]
            # Lookahead: if next value is greater, this is subtractive (IV, IX)
            if i + 1 < n and roman_map[s[i+1]] > val:
                total -= val
            else:
                total += val
        return total

    def int_to_minimal_roman(num):
        """Converts Integer to Minimal Roman string."""
        result = []
        for val, symbol in val_to_roman:
            while num >= val:
                result.append(symbol)
                num -= val
        return "".join(result)

    saved_chars = 0
    
    with open(filename, 'r') as f:
        for line in f:
            original = line.strip()
            if not original: continue
            
            # 1. Get value
            value = roman_to_int(original)
            
            # 2. Get minimal string
            minimal = int_to_minimal_roman(value)
            
            # 3. Calculate savings
            saved = len(original) - len(minimal)
            saved_chars += saved
            
            # Optional debug
            # if saved > 0:
            #     print(f"{original} ({len(original)}) -> {minimal} ({len(minimal)}) : Saved {saved}")

    print(f"Total characters saved: {saved_chars}")

if __name__ == "__main__":
    solve_roman_numerals()