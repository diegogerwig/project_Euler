"""
Project Euler Problem 100: Arranged Probability

Find the number of blue discs for the first arrangement that contains 
over 10^12 discs in total.

Equation: 2B(B-1) = N(N-1) => (2N-1)^2 - 2(2B-1)^2 = -1
Let X = 2N-1, Y = 2B-1.
Solve Pell equation: X^2 - 2Y^2 = -1
"""

def solve_arranged_probability():
    limit_total = 10**12
    
    # Fundamental solution for X^2 - 2Y^2 = -1
    # Corresponds to N=1, B=1 (trivial case)
    x = 1
    y = 1
    
    while True:
        # Generate next solution using recurrence
        # X_new = 3X + 4Y
        # Y_new = 2X + 3Y
        x_new = 3 * x + 4 * y
        y_new = 2 * x + 3 * y
        
        x = x_new
        y = y_new
        
        # Calculate Total discs (N) from X
        # X = 2N - 1  =>  N = (X + 1) / 2
        n = (x + 1) // 2
        
        if n > limit_total:
            # Calculate Blue discs (B) from Y
            # Y = 2B - 1  =>  B = (Y + 1) / 2
            b = (y + 1) // 2
            
            print(f"Total discs: {n}")
            print(f"Blue discs: {b}")
            break

if __name__ == "__main__":
    solve_arranged_probability()