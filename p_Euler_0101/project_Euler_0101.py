"""
Project Euler Problem 101: Optimum Polynomial

Find the sum of FITs (First Incorrect Terms) for the Bad Optimum Polynomials
for the sequence u_n = 1 - n + n^2 - ... + n^10.
"""

from fractions import Fraction

def solve_optimum_polynomial():
    # 1. Define the generating function
    def u(n):
        return sum((-n)**i for i in range(11))

    # Precompute the first few terms of the sequence
    # We need enough terms to verify. For k=10, we interpolate 1..10 and predict 11.
    # The actual sequence values will be used as y_j
    seq = [u(n) for n in range(1, 15)]
    
    total_fit_sum = 0
    
    print("Calculating FITs for k=1 to 10...")
    
    # 2. Loop through k (number of known terms)
    for k in range(1, 11):
        # We use points (x, y) for x = 1 to k
        # We want to predict y at target_x = k + 1
        target_x = k + 1
        prediction = Fraction(0, 1)
        
        # Lagrange Interpolation
        for j in range(k):
            x_j = j + 1      # 1-based index for x
            y_j = seq[j]     # 0-based index for y list
            
            # Compute basis polynomial L_j(target_x)
            numerator = 1
            denominator = 1
            
            for m in range(k):
                if m == j:
                    continue
                x_m = m + 1
                
                numerator *= (target_x - x_m)
                denominator *= (x_j - x_m)
            
            # Add contribution: y_j * (num / den)
            term = Fraction(numerator, denominator) * y_j
            prediction += term
            
        # The result must be an integer (it's a polynomial prediction for integer inputs)
        fit = int(prediction)
        total_fit_sum += fit
        
        # Optional: Print each step
        print(f"k={k}: Terms {seq[:k]} -> Predicts {fit} (Actual {seq[k]})")

    print("-" * 30)
    print(f"Sum of FITs: {total_fit_sum}")

if __name__ == "__main__":
    solve_optimum_polynomial()