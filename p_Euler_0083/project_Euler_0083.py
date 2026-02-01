"""
Project Euler Problem 83: Path Sum: Four Ways

Find the minimal path sum from top left to bottom right moving in any direction (up, down, left, right).
Method: Dijkstra's Algorithm.
"""

import urllib.request
import os
import heapq

def solve_path_sum_four_ways():
    # 1. Download/Read the file
    filename = 'p083_matrix.txt'
    url = 'https://projecteuler.net/project/resources/p083_matrix.txt'
    
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
    
    # 2. Dijkstra's Algorithm
    
    # Priority Queue stores tuples: (current_cost, row, col)
    # We start at (0,0) with cost equal to the cell value itself
    pq = [(matrix[0][0], 0, 0)]
    
    # Matrix to store the minimum cost found to reach each cell
    # Initialize with Infinity
    min_costs = [[float('inf')] * cols for _ in range(rows)]
    min_costs[0][0] = matrix[0][0]
    
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pq:
        # Get the cell with the lowest cost explored so far
        current_cost, r, c = heapq.heappop(pq)
        
        # Optimization: If we reached the target, we are done
        # (Because Dijkstra guarantees the first time you pop a node, it's the shortest path)
        if r == rows - 1 and c == cols - 1:
            print(f"Minimal path sum: {current_cost}")
            return
        
        # If we found a cheaper way to this cell already, skip processing
        if current_cost > min_costs[r][c]:
            continue
            
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = current_cost + matrix[nr][nc]
                
                # If this path is better than any previous path to neighbor
                if new_cost < min_costs[nr][nc]:
                    min_costs[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

if __name__ == "__main__":
    solve_path_sum_four_ways()