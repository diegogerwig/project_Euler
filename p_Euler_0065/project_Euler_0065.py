"""
Project Euler Problem 65: Convergents of e

The sequence of convergents for e is [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ...].
Find the sum of digits in the numerator of the 100th convergent.
"""

def solve_convergents_of_e():
    # 1. Generate the sequence of partial quotients (a_0 to a_99)
    # The pattern is: 2, then groups of (1, 2k, 1) for k=1, 2, 3...
    
    coeffs = [2] # a_0
    
    # We need 100 terms total. We already have 1.
    # Each iteration adds 3 terms. 33 iterations * 3 terms = 99 terms.
    # Total length = 1 + 99 = 100.
    for k in range(1, 34):
        coeffs.append(1)
        coeffs.append(2 * k)
        coeffs.append(1)
        
    # Trim just in case (though loop logic gives exactly 100 or 101)
    # The 100th convergent uses terms a_0 ... a_99
    coeffs = coeffs[:100]
    
    # 2. Calculate Numerators using Recurrence
    # h_n = a_n * h_{n-1} + h_{n-2}
    # Initial values for the recurrence engine:
    # Theoretically h_{-1} = 1, h_{-2} = 0
    
    h_prev = 1  # represents h_{n-1} initially (h_{-1})
    h_curr = 0  # represents h_{n-2} initially? No wait.
    
    # Let's verify manually for first steps:
    # h0 = a0 * 1 + 0 = 2. Correct.
    # h1 = a1 * h0 + h{-1} = 1 * 2 + 1 = 3. Correct.
    
    # Correct setup:
    n_minus_1 = 1 # h_{-1}
    n_minus_2 = 0 # h_{-2}
    
    numerator = 0
    
    for a in coeffs:
        numerator = a * n_minus_1 + n_minus_2
        
        # Shift variables for next step
        n_minus_2 = n_minus_1
        n_minus_1 = numerator
        
    # After the loop, 'numerator' holds h_99 (the 100th convergent's numerator)
    
    # 3. Sum the digits
    digit_sum = sum(int(d) for d in str(numerator))
    
    print(f"100th Convergent Numerator (first 20 digits): {str(numerator)[:20]}...")
    print(f"Sum of digits: {digit_sum}")

if __name__ == "__main__":
    solve_convergents_of_e()