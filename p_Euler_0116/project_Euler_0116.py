"""
Project Euler Problem 116: Red, Green or Blue Tiles

Row length: 50
Red tile length (m): 2
Green tile length (m): 3
Blue tile length (m): 4
Constraint: At least one colored tile must be used. Colors cannot be mixed.
"""

def count_ways(length, tile_size):
    # dynamic programming array
    # ways[i] stores the number of ways to tile a row of length i
    ways = [0] * (length + 1)
    
    # Base case: There is 1 way to tile a row of length 0 (empty)
    ways[0] = 1
    
    for i in range(1, length + 1):
        # Option 1: Place a grey tile (size 1)
        ways[i] += ways[i-1]
        
        # Option 2: Place a colored tile (size tile_size) if it fits
        if i >= tile_size:
            ways[i] += ways[i-tile_size]
            
    # Subtract 1 because the "all grey" solution is counted but valid only 
    # if we allow 0 colored tiles. The problem requires at least one.
    return ways[length] - 1

def solve_rgb_tiles():
    n = 50
    
    # Calculate ways for each color independently
    red_ways = count_ways(n, 2)
    green_ways = count_ways(n, 3)
    blue_ways = count_ways(n, 4)
    
    total = red_ways + green_ways + blue_ways
    
    print(f"Ways for Red (len 2): {red_ways}")
    print(f"Ways for Green (len 3): {green_ways}")
    print(f"Ways for Blue (len 4): {blue_ways}")
    print(f"Total distinct ways: {total}")

if __name__ == "__main__":
    solve_rgb_tiles()