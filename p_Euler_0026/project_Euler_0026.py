"""
Project Euler Problem 26: Reciprocal Cycles

A unit fraction contains 1 in the numerator.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.
"""

def get_cycle_length(d):
    """
    Calculates the length of the recurring cycle for 1/d using long division logic.
    """
    # Map to store the position where a remainder was first seen.
    # Format: { remainder: position }
    remainders = {}
    numerator = 1
    position = 0

    while numerator != 0:
        # If we have seen this numerator (remainder) before, we found a loop!
        if numerator in remainders:
            # The cycle length is the current position minus the first time we saw it.
            return position - remainders[numerator]
        
        # Save the position of this remainder
        remainders[numerator] = position
        
        # Perform long division step: multiply by 10 and get remainder
        numerator = (numerator * 10) % d
        position += 1
        
    # If numerator becomes 0, the division terminates (e.g., 1/2 = 0.5), so cycle is 0.
    return 0

def solve_reciprocal_cycles():
    longest_cycle = 0
    result_d = 0
    
    # Iterate denominators from 2 to 999
    # We check backwards from 999 because larger denominators usually (but not always)
    # produce larger cycles, but we must check all to be sure.
    for d in range(2, 1000):
        length = get_cycle_length(d)
        
        if length > longest_cycle:
            longest_cycle = length
            result_d = d
            
    print(f"The number d < 1000 with the longest recurring cycle is: {result_d}")
    print(f"Cycle length: {longest_cycle}")

if __name__ == "__main__":
    solve_reciprocal_cycles()