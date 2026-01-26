"""
Project Euler Problem 74: Digit Factorial Chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

# Precompute factorials 0-9
FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# Cache to store the chain length of numbers we've already solved
# Key: number, Value: length of non-repeating chain starting from key
chain_cache = {}

def get_next_val(n):
    """Calculates the sum of the factorials of the digits."""
    s = 0
    while n > 0:
        s += FACTORIALS[n % 10]
        n //= 10
    return s

def get_chain_length(n):
    """
    Returns the number of non-repeating terms in the chain starting at n.
    Uses caching to speed up processing.
    """
    original_n = n
    sequence = []
    
    # Generate chain until we hit a known number or a loop
    while n not in chain_cache:
        # Loop detection within the current sequence
        if n in sequence:
            # We hit a loop that is part of the current path.
            # Example: A -> B -> C -> B ...
            # The non-repeating terms are A, B, C.
            # The length is just the length of the sequence collected so far.
            
            # Optimization: We can cache all elements in this sequence now?
            # It's tricky because entering a loop at different points changes things.
            # For this problem, simple caching of the result for the START number is enough for speed.
            return len(sequence)
        
        sequence.append(n)
        n = get_next_val(n)
    
    # If we exited the loop because n is in chain_cache:
    # The total length is (steps taken so far) + (cached length of the number we hit)
    total_length = len(sequence) + chain_cache[n]
    
    # Store the result for the starting number (and potentially intermediates)
    # To keep logic simple and bug-free, we just return the calculation.
    # Caching the intermediates provides a speedup, but caching just the start 
    # is often sufficient. Let's cache the start.
    chain_cache[original_n] = total_length
    
    return total_length

def solve_digit_factorial_chains():
    limit = 1000000
    target_length = 60
    count = 0
    
    # Special case for 0? 0 -> 1 -> ...
    # Problem says "positive integer" usually, but 0! = 1 is defined.
    # Let's assume standard 1 to 999999 loop.
    
    # To optimize caching, we might want to fill the cache with the known loops first,
    # but the recursive logic handles it naturally.
    
    # However, because get_chain_length doesn't cache every intermediate step 
    # (to avoid complexity with partial loops), let's perform a 'trace' update.
    
    for i in range(1, limit):
        curr = i
        path = []
        
        while curr not in chain_cache and curr not in path:
            path.append(curr)
            curr = get_next_val(curr)
            
        if curr in chain_cache:
            length_from_curr = chain_cache[curr]
            # Back-propagate lengths
            for idx, val in enumerate(reversed(path)):
                chain_cache[val] = length_from_curr + idx + 1
        else:
            # We hit a loop within the current path (curr is in path)
            # Find where the loop starts
            loop_start_index = path.index(curr)
            
            # All numbers inside the loop have the same chain length (the loop size)
            # Wait, strictly speaking, the problem asks for "non-repeating terms".
            # If 169 -> 363601 -> 1454 -> 169, loop size is 3.
            # Chain length for 169 is 3. Chain length for 1454 is 3.
            
            # Nodes leading TO the loop:
            # 69 -> ... -> 169.
            # Their length is (distance to loop) + (loop size).
            
            loop_size = len(path) - loop_start_index
            
            # Assign lengths for items in the loop part
            for k in range(loop_start_index, len(path)):
                chain_cache[path[k]] = loop_size
                
            # Assign lengths for items leading to the loop
            for k in range(loop_start_index - 1, -1, -1):
                chain_cache[path[k]] = loop_size + (loop_start_index - k)

        if chain_cache[i] == target_length:
            count += 1
            
    print(f"Chains with exactly 60 non-repeating terms: {count}")

if __name__ == "__main__":
    solve_digit_factorial_chains()