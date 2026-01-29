"""
Project Euler Problem 68: Magic 5-gon Ring

Find the maximum 16-digit string for a "magic" 5-gon ring.
Constraints: 
1. Use numbers 1-10.
2. 10 must be in the outer ring (to get 16 digits).
3. Outer ring must be {6,7,8,9,10} to maximize the starting digit (min outer node = 6).
4. Inner ring must be {1,2,3,4,5}.
5. Each line sums to 14.
"""

import itertools

def solve_magic_5gon():
    # Inner ring numbers
    inner_nums = [1, 2, 3, 4, 5]
    target_sum = 14
    
    max_string = ""
    
    # Try all permutations of the inner ring
    for inner in itertools.permutations(inner_nums):
        # inner is a tuple like (1, 2, 3, 4, 5) representing the pentagon cycle
        # Lines are formed by:
        # (Ext_0, In_0, In_1)
        # (Ext_1, In_1, In_2)
        # ...
        # (Ext_4, In_4, In_0)
        
        outer = []
        valid = True
        
        # Calculate required outer nodes
        for i in range(5):
            # The two inner nodes for this line
            in_a = inner[i]
            in_b = inner[(i + 1) % 5] # Wrap around to 0 for the last one
            
            # Calculate what the outer node MUST be to hit the target sum
            ext = target_sum - (in_a + in_b)
            
            outer.append(ext)
        
        # Check if the calculated outer nodes are valid:
        # 1. Must be unique
        # 2. Must be within the set {6, 7, 8, 9, 10}
        # 3. No duplicates
        
        required_outer_set = {6, 7, 8, 9, 10}
        if set(outer) != required_outer_set:
            continue
            
        # If valid, construct the string
        # We must start from the group with the lowest external node
        
        # Find index of the lowest external node (which is 6)
        min_outer_idx = outer.index(min(outer))
        
        current_string = ""
        
        # Build string starting from that index and going clockwise (which is just increasing index)
        for i in range(5):
            idx = (min_outer_idx + i) % 5
            
            e = outer[idx]
            i1 = inner[idx]
            i2 = inner[(idx + 1) % 5]
            
            current_string += f"{e}{i1}{i2}"
            
        # Check if it's the maximum found so far
        if len(max_string) == 0 or current_string > max_string:
            max_string = current_string
            
    print(f"Maximum 16-digit string: {max_string}")

if __name__ == "__main__":
    solve_magic_5gon()