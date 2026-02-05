"""
Project Euler Problem 94: Almost Equilateral Triangles

Find the sum of the perimeters of all almost equilateral triangles 
with integral side lengths and area and whose perimeters do not exceed 1,000,000,000.

Equation: x^2 - 3y^2 = 4
Recurrence for x: x_k = 4 * x_{k-1} - x_{k-2}
Initial x: 2, 4
"""

def solve_almost_equilateral_triangles():
    limit_perimeter = 1_000_000_000
    total_perimeter_sum = 0
    
    # Initial values for x in x^2 - 3y^2 = 4
    # The sequence is 2, 4, 14, 52, 194...
    x_prev = 2
    x_curr = 4
    
    while True:
        # Generate next x using recurrence
        x_next = 4 * x_curr - x_prev
        
        # We start checking from x_next because 2 and 4 don't yield valid triangles
        # (they yield degenerate triangles with side 1 or 0 area)
        
        # Check if we exceeded limits roughly
        # Perimeter is roughly x_next
        if x_next > limit_perimeter + 2:
            break
            
        # Case 1: x = 3a + 1 (Corresponds to sides a, a, a-1)
        # We need x = 1 mod 3
        if (x_next - 1) % 3 == 0:
            a = (x_next - 1) // 3
            perimeter = 3 * a - 1
            # Check perimeter limit strict and area validity (area is guaranteed by Pell, but sides must be > 0)
            if perimeter <= limit_perimeter and perimeter > 0:
                total_perimeter_sum += perimeter
                
        # Case 2: x = 3a - 1 (Corresponds to sides a, a, a+1)
        # We need x = 2 mod 3 (or -1 mod 3)
        if (x_next + 1) % 3 == 0:
            a = (x_next + 1) // 3
            perimeter = 3 * a + 1
            if perimeter <= limit_perimeter and perimeter > 0:
                total_perimeter_sum += perimeter

        # Advance sequence
        x_prev = x_curr
        x_curr = x_next
        
    print(f"Sum of perimeters: {total_perimeter_sum}")

if __name__ == "__main__":
    solve_almost_equilateral_triangles()