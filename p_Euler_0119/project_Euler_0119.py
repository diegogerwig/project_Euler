"""
Project Euler Problem 119: Digit Power Sum

The number 512 is interesting because it is equal to the sum of its digits raised to some power:
5 + 1 + 2 = 8, and 8^3 = 512.
Find a_30.
"""

def sum_digits(n):
    """Calculates the sum of the digits of n."""
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def solve_digit_power_sum():
    target_index = 30
    candidates = []
    
    # We estimate limits based on the problem scale.
    # Base: The sum of digits. 
    # For a number around 10^15, max sum of digits is 9*15 = 135.
    # Iterating base up to 200 is extremely safe.
    
    for base in range(2, 200):
        n = base
        # Iterate exponents starting from 2
        for exponent in range(2, 20): # 2^20 is already > 1 million, sufficient range check
            n *= base
            
            # The problem asks for numbers with at least two digits
            if n < 10:
                continue
                
            # Soft upper limit to prevent numbers getting too huge unnecessarily
            # We can refine this if we don't find 30 terms, but 10^18 is plenty.
            if n > 10**16:
                break
            
            # THE CORE CHECK:
            # Does the sum of digits of this power actually equal the base?
            if sum_digits(n) == base:
                candidates.append(n)
    
    # Sort the found numbers to find the correct order
    candidates.sort()
    
    # Remove duplicates if any (though logic implies uniqueness for distinct (b,e) usually)
    # but strictly speaking 2^4 = 4^2, so sums might collide? 
    # Actually base is derived from sum, so if sum(16)=7 != 2, sum(16)=7 != 4.
    # So uniqueness is likely guaranteed by the property check, but let's be safe.
    unique_candidates = sorted(list(set(candidates)))
    
    if len(unique_candidates) >= target_index:
        result = unique_candidates[target_index - 1] # 0-indexed
        print(f"The {target_index}th term is: {result}")
        
        # Verification with examples from problem description
        # a_2 = 512
        if len(unique_candidates) >= 2:
            print(f"Verification a_2: {unique_candidates[1]} (Expected 512)")
        # a_10 = 614656
        if len(unique_candidates) >= 10:
            print(f"Verification a_10: {unique_candidates[9]} (Expected 614656)")

    else:
        print(f"Insufficient search range. Found only {len(unique_candidates)} terms.")

if __name__ == "__main__":
    solve_digit_power_sum()