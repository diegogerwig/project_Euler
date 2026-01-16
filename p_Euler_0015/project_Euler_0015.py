"""
Project Euler Problem 15: Lattice Paths

Starting in the top left corner of a 2x2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import math

def solve_lattice_paths():
    """
    Calculates the number of lattice paths in a grid using Combinatorics.
    
    Logic:
    To traverse an N x N grid from top-left to bottom-right moving only 
    Right (R) and Down (D), you must make exactly 2*N moves in total.
    Exactly N of those moves must be 'Right' and N must be 'Down'.
    
    This becomes a permutation problem with repetition, or simply a 
    combination problem: "Choose N moves to be 'Right' out of 2*N total moves".
    
    Formula: (2n)! / (n! * n!)  OR  nCr(2n, n)
    """
    
    grid_size = 20
    
    # Total moves required to cross the grid (Right + Down)
    total_moves = grid_size * 2  # 40 moves for a 20x20 grid
    
    # We need to choose 'grid_size' moves to be Right (or Down)
    # math.comb(n, k) returns the number of ways to choose k items from n.
    # Available in Python 3.8+
    routes = math.comb(total_moves, grid_size)
    
    print(f"Grid size: {grid_size}x{grid_size}")
    print(f"Total steps required: {total_moves}")
    print(f"Number of possible routes: {routes}")

if __name__ == "__main__":
    solve_lattice_paths()