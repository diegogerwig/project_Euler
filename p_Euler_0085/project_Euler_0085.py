"""
Project Euler Problem 85: Counting Rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 
contains eighteen rectangles.
Find the area of the grid with the nearest solution to 2,000,000 rectangles.

Formula for rectangles in w*h grid:
(w * (w + 1) / 2) * (h * (h + 1) / 2)
"""

def solve_counting_rectangles():
    target = 2000000
    closest_diff = float('inf')
    best_area = 0
    
    # Upper bound logic:
    # Even if h=1, w would need to be around 2000 to reach 2 million.
    # So searching up to 2000 is more than enough.
    limit = 2000
    
    for w in range(1, limit):
        for h in range(1, w + 1): # We can assume h <= w due to symmetry
            
            # Calculate number of rectangles
            # Using integer division //
            rects = (w * (w + 1) * h * (h + 1)) // 4
            
            diff = abs(target - rects)
            
            if diff < closest_diff:
                closest_diff = diff
                best_area = w * h
                # Optional debug print
                # print(f"New best: {w}x{h} (Area: {best_area}) -> {rects} rectangles (Diff: {diff})")
            
            # Optimization:
            # If rects is already way bigger than target, increasing h will only
            # make it bigger. So we can break the inner loop.
            if rects > target:
                break
                
    print(f"Area of the grid with the nearest solution: {best_area}")

if __name__ == "__main__":
    solve_counting_rectangles()