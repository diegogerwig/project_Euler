"""
Project Euler Problem 99: Largest Exponential

Determine which line number in base_exp.txt has the greatest numerical value.
Strategy: Use logarithms to compare magnitudes.
log(b^e) = e * log(b)
"""

import math
import os
import urllib.request

def solve_largest_exponential():
    # 1. Download/Read the file
    filename = 'p099_base_exp.txt'
    url = 'https://projecteuler.net/project/resources/p099_base_exp.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    max_magnitude = 0
    max_line_number = 0

    with open(filename, 'r') as f:
        # Enumerate gives us (index, line). Start index at 1 for line numbers.
        for line_num, line in enumerate(f, 1):
            parts = line.strip().split(',')
            base = int(parts[0])
            exponent = int(parts[1])
            
            # Calculate magnitude using log
            # We can use math.log (natural log) or math.log10. The comparison holds either way.
            magnitude = exponent * math.log(base)
            
            if magnitude > max_magnitude:
                max_magnitude = magnitude
                max_line_number = line_num
                # Optional: Print new records to see progress
                # print(f"New max at line {line_num}: {base}^{exponent}")

    print("-" * 30)
    print(f"Line with the largest numerical value: {max_line_number}")

if __name__ == "__main__":
    solve_largest_exponential()