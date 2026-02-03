"""
Project Euler Problem 91: Right Triangles with Integer Coordinates

Goal: Count the number of right triangles OPQ where 0 <= x,y <= 50.
"""

import math

def solve_right_triangles():
    size = 50
    
    # 1. Base cases involving axes
    # - Right angle at Origin (0,0): P on x-axis, Q on y-axis -> size * size
    # - Right angle at P where P is on x-axis: P(x,0), Q(x,y) -> size * size
    # - Right angle at P where P is on y-axis: P(0,y), Q(x,y) -> size * size
    # Total trivial cases = 3 * size^2
    count = 3 * size * size
    
    # 2. Cases where the right angle is at a point P(x,y) strictly inside the grid
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            # Calculate the reduced slope components of OP
            g = math.gcd(x, y)
            dx = x // g
            dy = y // g
            
            # The slope of PQ must be perpendicular to OP.
            # OP slope = dy/dx (actual y/x).
            # PQ slope = -dx/dy.
            # This means integer steps for Q are (-dy, dx) or (dy, -dx).
            
            # Direction 1: Up and Left
            # x decreases by dy, y increases by dx
            # Constraints: x - k*dy >= 0  => k <= x/dy
            #              y + k*dx <= size => k <= (size-y)/dx
            steps_dir1 = min(x // dy, (size - y) // dx)
            
            # Direction 2: Down and Right
            # x increases by dy, y decreases by dx
            # Constraints: x + k*dy <= size => k <= (size-x)/dy
            #              y - k*dx >= 0    => k <= y/dx
            steps_dir2 = min((size - x) // dy, y // dx)
            
            count += steps_dir1 + steps_dir2
            
    print(f"Total right triangles: {count}")

if __name__ == "__main__":
    solve_right_triangles()