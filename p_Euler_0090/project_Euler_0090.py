"""
Project Euler Problem 90: Cube Digit Pairs

Objective: Count distinct arrangements of two cubes that can display all square numbers below 100.
Rule: 6 and 9 are interchangeable.
"""

from itertools import combinations

def solve_cube_digit_pairs():
    # 1. Generate all possible unique cubes (combinations of 6 digits)
    digits = range(10)
    cubes = list(combinations(digits, 6))
    
    # 2. Define the target squares as pairs of digits
    # Note: 01, 04, 09 require the '0' digit.
    targets = [
        (0, 1), (0, 4), (0, 9),
        (1, 6), (2, 5), (3, 6),
        (4, 9), (6, 4), (8, 1)
    ]
    
    valid_arrangements = 0
    
    # 3. Iterate through all unique pairs of cubes
    # We use range(i, len) to include pairs of identical cubes and ignore order (C1, C2) == (C2, C1)
    for i in range(len(cubes)):
        for j in range(i, len(cubes)):
            
            # Create sets for easier lookup
            c1 = set(cubes[i])
            c2 = set(cubes[j])
            
            # Apply the 6/9 flip rule
            # If a cube has 6, it can also represent 9.
            # If a cube has 9, it can also represent 6.
            if 6 in c1: c1.add(9)
            if 9 in c1: c1.add(6)
            
            if 6 in c2: c2.add(9)
            if 9 in c2: c2.add(6)
            
            # 4. Verify all squares
            all_possible = True
            for d1, d2 in targets:
                # Can we form the number d1 d2?
                # Check: (d1 on C1 AND d2 on C2) OR (d1 on C2 AND d2 on C1)
                can_form_current = (
                    (d1 in c1 and d2 in c2) or 
                    (d1 in c2 and d2 in c1)
                )
                
                if not can_form_current:
                    all_possible = False
                    break
            
            if all_possible:
                valid_arrangements += 1
                
    print(f"Number of distinct arrangements: {valid_arrangements}")

if __name__ == "__main__":
    solve_cube_digit_pairs()