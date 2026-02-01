"""
Project Euler Problem 96: Su Doku

By solving all fifty puzzles find the sum of the 3-digit numbers 
found in the top left corner of each solution grid.

Method: Recursive Backtracking.
"""

import os
import urllib.request

def is_valid(grid, row, col, num):
    """
    Check if putting 'num' at grid[row][col] is valid
    according to Sudoku rules.
    """
    # Check Row
    for x in range(9):
        if grid[row][x] == num:
            return False
            
    # Check Column
    for x in range(9):
        if grid[x][col] == num:
            return False
            
    # Check 3x3 Box
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
                
    return True

def solve(grid):
    """
    Solves the Sudoku grid in-place using backtracking.
    Returns True if solvable, False otherwise.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0: # Find empty cell
                
                # Try numbers 1-9
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        
                        if solve(grid):
                            return True
                        
                        # Backtrack: If the path didn't work, reset to 0
                        grid[row][col] = 0
                
                return False # Trigger backtracking
    return True # No empty cells left, puzzle solved

def solve_sudoku_problem():
    # 1. Download/Read the file
    filename = 'p096_sudoku.txt'
    url = 'https://projecteuler.net/project/resources/p096_sudoku.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    total_sum = 0
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Process 50 grids
    # Each grid takes 10 lines (1 header + 9 rows)
    for i in range(0, len(lines), 10):
        # Extract the 9x9 grid
        # Skip the "Grid XX" line (lines[i])
        grid_lines = lines[i+1 : i+10]
        
        grid = []
        for line in grid_lines:
            # Convert string "00302..." to list of ints [0, 0, 3, 0, 2...]
            row = [int(ch) for ch in line.strip()]
            grid.append(row)
            
        # Solve the grid
        solve(grid)
        
        # Extract the 3-digit number from top-left (0,0), (0,1), (0,2)
        top_left_num = int(f"{grid[0][0]}{grid[0][1]}{grid[0][2]}")
        total_sum += top_left_num
        
        # Optional progress indicator
        # print(f"Solved Grid {i//10 + 1}: Top-left = {top_left_num}")

    print(f"Sum of the 3-digit numbers found in the top left corner: {total_sum}")

if __name__ == "__main__":
    solve_sudoku_problem()