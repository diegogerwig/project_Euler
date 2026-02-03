"""
Project Euler Problem 95: Amicable Chains

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

def solve_amicable_chains():
    limit = 1000000
    
    # 1. Precompute sum of proper divisors using a sieve-like method
    # Initialize with 1 because 1 is a proper divisor for all n > 1
    sum_divs = [1] * (limit + 1)
    sum_divs[0] = 0 # Not used
    sum_divs[1] = 0 # Proper divisors of 1 sum to 0
    
    # Iterate from 2 to limit/2
    for i in range(2, limit // 2 + 1):
        # Add i to all its multiples
        for j in range(2 * i, limit + 1, i):
            sum_divs[j] += i
            
    # 2. Find longest chain
    visited_globally = [False] * (limit + 1)
    max_chain_length = 0
    smallest_member_of_best_chain = 0
    
    for i in range(2, limit + 1):
        # Optimization: If we already processed this number in a previous chain, skip
        if visited_globally[i]:
            continue
            
        chain = []
        current = i
        in_current_path = {} # Map number -> index in current chain list
        
        while True:
            chain.append(current)
            in_current_path[current] = len(chain) - 1
            visited_globally[current] = True
            
            next_val = sum_divs[current]
            
            # Invalid conditions
            if next_val > limit or next_val == 0:
                # Chain breaks (exceeds limit or hits 0 like primes)
                break
            
            if next_val in in_current_path:
                # Cycle detected!
                # The cycle might be smaller than the full path (e.g. tail -> cycle)
                # We extract just the cyclic part
                start_index = in_current_path[next_val]
                cycle_part = chain[start_index:]
                cycle_len = len(cycle_part)
                
                if cycle_len > max_chain_length:
                    max_chain_length = cycle_len
                    smallest_member_of_best_chain = min(cycle_part)
                    # Optional debug
                    # print(f"New best chain length: {cycle_len}, Smallest member: {smallest_member_of_best_chain}, Chain: {cycle_part}")
                break
            
            if visited_globally[next_val]:
                # Merged into an old path we already processed
                break
                
            current = next_val

    print(f"Longest chain length: {max_chain_length}")
    print(f"Smallest member of the longest amicable chain: {smallest_member_of_best_chain}")

if __name__ == "__main__":
    solve_amicable_chains()