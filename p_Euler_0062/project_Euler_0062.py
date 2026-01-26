"""
Project Euler Problem 62: Cubic Permutations

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly three permutations 
of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

def solve_cubic_permutations():
    # Start iterating n from 1
    n = 1
    
    # Map structure:
    # Key: sorted string of digits (signature)
    # Value: list of cubes found with that signature
    permutations = {}
    
    # We track the number of digits of the cubes we are currently processing
    current_digit_len = 0
    
    while True:
        cube = n ** 3
        s_cube = str(cube)
        d_len = len(s_cube)
        
        # If the length of digits has increased, it means we finished 
        # checking all cubes of the previous length.
        # Now we check if we found the solution in the previous batch.
        if d_len > current_digit_len:
            
            # Look for any group with exactly 5 members
            candidates = []
            for signature, cubes_list in permutations.items():
                if len(cubes_list) == 5:
                    # We want the smallest cube in the family
                    candidates.append(min(cubes_list))
            
            # If we found candidates, the smallest of them is the global answer
            if candidates:
                result = min(candidates)
                print(f"Solution found!")
                print(f"Smallest cube: {result}")
                print(f"Root: {round(result**(1/3))}")
                
                # Optional: Show the full family for verification
                # Find the key for this result
                key_sig = "".join(sorted(str(result)))
                print(f"Family of 5 cubes: {permutations[key_sig]}")
                return
            
            # Reset for the new digit length
            permutations = {}
            current_digit_len = d_len
            
        # Add the current cube to the map
        # Signature is the sorted digits: 41063625 -> "01234566"
        signature = "".join(sorted(s_cube))
        
        if signature not in permutations:
            permutations[signature] = []
        permutations[signature].append(cube)
        
        n += 1

if __name__ == "__main__":
    solve_cubic_permutations()