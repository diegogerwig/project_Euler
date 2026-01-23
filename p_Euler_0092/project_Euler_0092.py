"""
Project Euler Problem 92: Square Digit Chains

A number chain is created by continuously adding the square of the digits.
Every starting number eventually arrives at 1 or 89.
How many starting numbers below ten million will arrive at 89?
"""

def solve_square_digit_chains():
    limit = 10000000
    
    # The maximum sum of squares for a number < 10,000,000 is for 9,999,999:
    # 9^2 * 7 = 567.
    # So every chain will quickly fall below 568.
    # We can cache the result for all numbers up to 567.
    
    # 0 = unknown, 1 = ends in 1, 89 = ends in 89
    # We use a simple array for memoization
    cache = [0] * 568
    cache[1] = 1
    cache[89] = 89
    
    def get_destination(n):
        if n == 1 or n == 89:
            return n
        if cache[n] != 0:
            return cache[n]
        
        # Calculate next step
        next_val = sum(int(d)**2 for d in str(n))
        
        # Recursive call
        dest = get_destination(next_val)
        
        # Memoize
        cache[n] = dest
        return dest

    # 1. Pre-fill the cache for small numbers (1 to 567)
    for i in range(1, 568):
        get_destination(i)
        
    # 2. Check all numbers up to limit
    count_89 = 0
    
    # Optimization: Pre-calculate squares of digits 0-9 to avoid re-multiplying
    squares = [d*d for d in range(10)]
    
    print("Counting chains ending in 89...")
    
    for i in range(1, limit):
        # Calculate sum of squares manually or via string
        # String method is slightly slower but easier to read.
        # For Python, it's fast enough (10M iterations ~ 5-10 seconds)
        
        # Efficient sum of squares without string conversion for speed:
        temp = i
        current_sum = 0
        while temp > 0:
            current_sum += squares[temp % 10]
            temp //= 10
            
        # The current_sum is definitely <= 567, so we look it up directly
        if cache[current_sum] == 89:
            count_89 += 1
            
    print(f"Total numbers arriving at 89: {count_89}")

if __name__ == "__main__":
    solve_square_digit_chains()