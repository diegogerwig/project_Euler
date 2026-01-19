"""
Project Euler Problem 39: Integer Right Triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

def solve_integer_right_triangles():
    max_solutions = 0
    best_p = 0
    
    # 1. Iterate through possible perimeters
    # We only check even numbers because the perimeter of an integer 
    # right triangle is always even.
    for p in range(2, 1001, 2):
        
        current_solutions = 0
        
        # 2. Iterate through possible values for side 'a'
        # 'a' must be less than p/3 because a < b < c and a+b+c = p
        for a in range(2, int(p/3) + 1):
            
            # 3. Check if a valid integer 'b' exists for this 'a' and 'p'
            # Derived from a^2 + b^2 = (p - a - b)^2
            # Formula: b = (p^2 - 2pa) / (2p - 2a)
            
            numerator = p**2 - 2*p*a
            denominator = 2*p - 2*a
            
            # If division is clean (remainder 0), we found an integer side 'b'
            if numerator % denominator == 0:
                current_solutions += 1
                
        # 4. Update Maximum
        if current_solutions > max_solutions:
            max_solutions = current_solutions
            best_p = p
            
    print(f"The perimeter p with max solutions is: {best_p}")
    print(f"Number of solutions found: {max_solutions}")

if __name__ == "__main__":
    solve_integer_right_triangles()