"""
Project Euler Problem 28: Number Spiral Diagonals

Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed.
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?
"""

def solve_number_spiral():
    # 1. Configuration
    grid_size = 1001
    
    # Start with the center number '1', which is the center of the diagonals.
    total_sum = 1
    
    # 2. Iterate through the layers
    # We start from a 3x3 square, then 5x5, up to 1001x1001.
    # The step is 2 because the width increases by 2 each layer.
    for n in range(3, grid_size + 1, 2):
        
        # The Top-Right corner is always n squared
        top_right = n * n
        
        # The distance between corners in the current layer is (n - 1)
        gap = n - 1
        
        # Calculate the other three corners by subtracting the gap
        top_left = top_right - gap
        bottom_left = top_right - (gap * 2)
        bottom_right = top_right - (gap * 3)
        
        # Add the four corners to the sum
        layer_sum = top_right + top_left + bottom_left + bottom_right
        total_sum += layer_sum

    print(f"Grid size: {grid_size}x{grid_size}")
    print(f"Sum of diagonals: {total_sum}")

if __name__ == "__main__":
    solve_number_spiral()