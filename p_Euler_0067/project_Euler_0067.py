"""
Project Euler Problem 67: Maximum Path Sum II

The logic is identical to Problem 18 (Bottom-Up Dynamic Programming),
but we must handle a much larger dataset loaded from a file.
"""

import urllib.request
import os

def solve_maximum_path_sum_ii():
    # 1. File Configuration
    filename = 'p067_triangle.txt'
    url = 'https://projecteuler.net/project/resources/p067_triangle.txt'
    
    # 2. Download the file if missing (Auto-download)
    if not os.path.exists(filename):
        print("Downloading triangle file from Project Euler...")
        try:
            urllib.request.urlretrieve(url, filename)
            print("Download successful.")
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    # 3. Read and Parse the Data
    # We convert the text file into a List of Lists of Integers
    triangle = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # "59 30 70" -> [59, 30, 70]
            row = [int(x) for x in line.split()]
            triangle.append(row)

    print(f"Triangle loaded with {len(triangle)} rows.")

    # 4. The Algorithm (Bottom-Up Approach)
    # Start from the second-to-last row and move up to the tip.
    # We fold the triangle upwards, always choosing the larger path below.
    
    total_rows = len(triangle)
    
    # Loop backwards from row 98 to 0
    for i in range(total_rows - 2, -1, -1):
        for j in range(len(triangle[i])):
            
            # Look at the two numbers below
            left_child = triangle[i+1][j]
            right_child = triangle[i+1][j+1]
            
            # Add the larger one to the current cell
            triangle[i][j] += max(left_child, right_child)

    # 5. The Result
    # The top element (triangle[0][0]) now holds the maximum possible sum.
    print(f"Maximum path sum: {triangle[0][0]}")

if __name__ == "__main__":
    solve_maximum_path_sum_ii()