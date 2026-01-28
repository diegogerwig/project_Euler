"""
Project Euler Problem 206: Concealed Square

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0.
Logic:
The number must end in 0, so x^2 ends in 00.
We look for n such that n^2 follows pattern 1_2_3_4_5_6_7_8_9.
n must end in 3 or 7.
"""

def solve_concealed_square():
    # Min value: sqrt(10203040506070809) -> approx 101010101
    # Max value: sqrt(19293949596979899) -> approx 138902663
    
    # We start from the top and go down (arbitrary choice, works either way)
    # We start at the nearest number ending in 3 or 7 near the max bound.
    n = 138902663 
    
    while n >= 101010101:
        square_str = str(n * n)
        
        # Check the pattern by verifying digits at even indices
        # 1 _ 2 _ 3 _ 4 _ 5 _ 6 _ 7 _ 8 _ 9
        # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 (Index)
        if (square_str[0] == '1' and
            square_str[2] == '2' and
            square_str[4] == '3' and
            square_str[6] == '4' and
            square_str[8] == '5' and
            square_str[10] == '6' and
            square_str[12] == '7' and
            square_str[14] == '8' and
            square_str[16] == '9'):
            
            # Found it! Remember to multiply by 10 for the final answer
            print(f"Base number found: {n}")
            print(f"Solution (x): {n}0")
            print(f"Verification (x^2): {n}0^2 = {square_str}00")
            return

        # Optimization: Jump between numbers ending in 3 and 7
        # If n ends in 3, previous valid is n-6 (ends in 7)
        # If n ends in 7, previous valid is n-4 (ends in 3)
        if n % 10 == 3:
            n -= 6
        else:
            n -= 4

if __name__ == "__main__":
    solve_concealed_square()