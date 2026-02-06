"""
Project Euler Problem 93: Arithmetic Expressions

Find the set of four distinct digits for which the longest set of consecutive 
positive integers, 1 to n, can be obtained.
"""

import itertools

def solve_arithmetic_expressions():
    # Define arithmetic operations
    # Using lambda functions for cleaner evaluation logic
    # Division returns None if division by zero occurs
    ops = [
        lambda x, y: x + y,
        lambda x, y: x - y,
        lambda x, y: x * y,
        lambda x, y: x / y if y != 0 else None
    ]
    
    max_consecutive = 0
    best_digits = ""
    
    # 1. Iterate over all unique combinations of 4 digits (e.g., {1, 2, 3, 4})
    # Since we need the output as 'abcd', we iterate sorted tuples (0..9)
    for digits in itertools.combinations(range(10), 4):
        generated_values = set()
        
        # 2. Iterate over all permutations of these digits (Order matters for -, /)
        for d in itertools.permutations(digits):
            
            # 3. Iterate over all combinations of 3 operators
            for op1, op2, op3 in itertools.product(ops, repeat=3):
                
                # We need to evaluate the 5 distinct binary tree shapes for 4 leaves
                try:
                    # Shape 1: ((a op1 b) op2 c) op3 d
                    v1 = op1(d[0], d[1])
                    if v1 is not None:
                        v2 = op2(v1, d[2])
                        if v2 is not None:
                            res = op3(v2, d[3])
                            if res is not None: generated_values.add(res)
                            
                    # Shape 2: (a op1 b) op2 (c op3 d)
                    v1 = op1(d[0], d[1])
                    v2 = op3(d[2], d[3])
                    if v1 is not None and v2 is not None:
                        res = op2(v1, v2)
                        if res is not None: generated_values.add(res)
                        
                    # Shape 3: (a op1 (b op2 c)) op3 d
                    v1 = op2(d[1], d[2])
                    if v1 is not None:
                        v2 = op1(d[0], v1)
                        if v2 is not None:
                            res = op3(v2, d[3])
                            if res is not None: generated_values.add(res)
                            
                    # Shape 4: a op1 ((b op2 c) op3 d)
                    v1 = op2(d[1], d[2])
                    if v1 is not None:
                        v2 = op3(v1, d[3])
                        if v2 is not None:
                            res = op1(d[0], v2)
                            if res is not None: generated_values.add(res)
                            
                    # Shape 5: a op1 (b op2 (c op3 d))
                    v1 = op3(d[2], d[3])
                    if v1 is not None:
                        v2 = op2(d[1], v1)
                        if v2 is not None:
                            res = op1(d[0], v2)
                            if res is not None: generated_values.add(res)

                except Exception:
                    pass

        # 4. Check consecutive sequence 1 to n
        # Because division creates floats (e.g., 3.0), we check with small epsilon tolerance
        current_len = 0
        for i in itertools.count(1):
            # Check if integer 'i' is in our generated float values
            found = False
            for val in generated_values:
                # Must be positive integer (val > 0 already implicit by range start 1)
                # Check if val is effectively an integer equal to i
                if abs(val - i) < 1e-9:
                    found = True
                    break
            
            if found:
                current_len += 1
            else:
                break
        
        # 5. Update Max
        if current_len > max_consecutive:
            max_consecutive = current_len
            best_digits = "".join(str(x) for x in digits)
            # print(f"Found new best: {best_digits} -> 1 to {current_len}")

    print(f"Set of digits: {best_digits}")
    print(f"Longest consecutive sequence length: {max_consecutive}")

if __name__ == "__main__":
    solve_arithmetic_expressions()