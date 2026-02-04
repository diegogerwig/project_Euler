"""
Project Euler Problem 124: Ordered Radicals

Calculate rad(n) for 1 <= n <= 100,000.
Sort the numbers based on (rad(n), n).
Find the 10,000th element E(10000).
"""

def solve_ordered_radicals():
    limit = 100000
    target_index = 10000
    
    # 1. Initialize rad array
    # rad[n] will store the product of distinct prime factors of n.
    # Initialize with 1.
    rad = [1] * (limit + 1)
    
    # 2. Sieve-like process to compute rad(n)
    for i in range(2, limit + 1):
        # If rad[i] is 1, then i is prime
        if rad[i] == 1:
            # Multiply i into the radical of all its multiples
            for j in range(i, limit + 1, i):
                rad[j] *= i
                
    # 3. Create a list of (rad(n), n) pairs to sort
    # We start from n=1
    data = []
    for n in range(1, limit + 1):
        data.append((rad[n], n))
        
    # 4. Sort
    # Python sorts tuples element by element:
    # First by rad[n], then by n. Exactly what we need.
    data.sort()
    
    # 5. Get the 10,000th element
    # The problem uses 1-based indexing, so we want index 9999
    result_tuple = data[target_index - 1]
    
    print(f"E({target_index}): n = {result_tuple[1]} (rad = {result_tuple[0]})")

if __name__ == "__main__":
    solve_ordered_radicals()