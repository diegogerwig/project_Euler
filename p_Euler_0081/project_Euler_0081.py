"""
Project Euler Problem 81: Path Sum: Two Ways

In the 80 by 80 matrix, find the minimal path sum from the top left 
to the bottom right by only moving right and down.
"""

import urllib.request
import os

def solve_path_sum_two_ways():
    # 1. Download/Read the file
    filename = 'p081_matrix.txt'
    url = 'https://projecteuler.net/project/resources/p081_matrix.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    # Read matrix into a 2D list
    with open(filename, 'r') as f:
        matrix = [[int(n) for n in line.strip().split(',')] for line in f]
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    # 2. Dynamic Programming
    # We update the matrix in-place to store the cumulative minimum sums.
    
    # Base case: The top-left cell remains as is.
    
    # Initialize the first row (can only come from the left)
    for j in range(1, cols):
        matrix[0][j] += matrix[0][j-1]
        
    # Initialize the first column (can only come from above)
    for i in range(1, rows):
        matrix[i][0] += matrix[i-1][0]
        
    # Fill the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            # The cost to reach (i, j) is the cell value + min of Top or Left neighbor
            min_prev = min(matrix[i-1][j], matrix[i][j-1])
            matrix[i][j] += min_prev
            
    # The bottom-right cell now contains the minimal path sum
    result = matrix[rows-1][cols-1]
    print(f"Minimal path sum: {result}")

if __name__ == "__main__":
    solve_path_sum_two_ways()