"""
Project Euler Problem 145: Reversible Numbers

Objective: How many reversible numbers are there below one-billion?
Definition: n + reverse(n) consists entirely of odd digits.
Constraint: Leading zeros not allowed in n or reverse(n) (n % 10 != 0).

Method: Combinatorial counting based on digit length properties.
"""

def solve_reversible_numbers():
    total_reversible = 0
    limit_power = 9  # We need to check numbers with 1 to 9 digits
    
    print("Calculating reversible numbers by digit length:")
    
    for length in range(1, limit_power + 1):
        count = 0
        
        # Case 1: Odd number of digits
        if length % 2 != 0:
            # Sub-case: length % 4 == 1 (1, 5, 9)
            # The middle digit (n + n) is always even. Even with a carry, 
            # carry propagation implies an even digit elsewhere for these lengths.
            if length % 4 == 1:
                count = 0
            
            # Sub-case: length % 4 == 3 (3, 7)
            # Formula: 100 * 500^((n-3)/4)
            elif length % 4 == 3:
                power = (length - 3) // 4
                count = 100 * (500 ** power)
        
        # Case 2: Even number of digits (2, 4, 6, 8)
        else:
            # Formula: 20 * 30^((n/2)-1)
            power = (length // 2) - 1
            count = 20 * (30 ** power)
            
        print(f"  Length {length}: {count}")
        total_reversible += count

    print("-" * 30)
    print(f"Total reversible numbers below 1 billion: {total_reversible}")

if __name__ == "__main__":
    solve_reversible_numbers()