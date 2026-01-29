"""
Project Euler Problem 82: Path Sum: Three Ways

Find the minimal path sum from the left column to the right column,
moving only up, down, and right.
"""

import urllib.request
import os

def solve_path_sum_three_ways():
    # 1. Download/Read the file
    filename = 'p082_matrix.txt'
    url = 'https://projecteuler.net/project/resources/p082_matrix.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    # Read matrix
    with open(filename, 'r') as f:
        matrix = [[int(n) for n in line.strip().split(',')] for line in f]
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    # 2. Dynamic Programming
    # We maintain a list 'dp' that stores the minimum cost to reach 
    # the current column's cells.
    
    # Initial state: The cost to reach the first column is just the value of the cells.
    dp = [matrix[i][0] for i in range(rows)]
    
    # Iterate through each subsequent column
    for j in range(1, cols):
        new_dp = [0] * rows
        
        # Step A: Initialize new_dp with the cost of coming directly from the LEFT
        for i in range(rows):
            new_dp[i] = dp[i] + matrix[i][j]
            
        # Step B: Sweep DOWN
        # Check if it's cheaper to come from the cell above in the current column
        for i in range(1, rows):
            new_dp[i] = min(new_dp[i], new_dp[i-1] + matrix[i][j])
            
        # Step C: Sweep UP
        # Check if it's cheaper to come from the cell below in the current column
        for i in range(rows - 2, -1, -1):
            new_dp[i] = min(new_dp[i], new_dp[i+1] + matrix[i][j])
            
        # Update dp for the next iteration
        dp = new_dp
        
    # The answer is the minimum value in the last column
    result = min(dp)
    print(f"Minimal path sum: {result}")

if __name__ == "__main__":
    solve_path_sum_three_ways()