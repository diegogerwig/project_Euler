"""
Project Euler Problem 50: Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:
2 + 3 + 5 + 7 + 11 + 13 = 41

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

def solve_consecutive_prime_sum():
    limit = 1000000
    
    # 1. Sieve of Eratosthenes to get primes and fast lookup
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False
                
    primes = [i for i, p in enumerate(is_prime) if p]
    
    # 2. Precompute Cumulative Sums (Prefix Sums)
    # prime_sums[k] = sum of the first k primes
    # This allows calculating sum(primes[i:j]) as prime_sums[j] - prime_sums[i]
    prime_sums = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        prime_sums[i+1] = prime_sums[i] + primes[i]
        
    # 3. Find the maximum possible length
    # If we sum from the smallest prime (2), how many does it take to exceed limit?
    max_length = 0
    for i, total in enumerate(prime_sums):
        if total >= limit:
            max_length = i
            break
            
    print(f"Max theoretical chain length: {max_length}")
    
    # 4. Search for the longest chain (Descending order)
    # We iterate length downwards. The first valid prime we find is the winner.
    for length in range(max_length, 0, -1):
        
        # Sliding window
        # We try sequences of 'length' starting from index i
        for i in range(len(primes) - length):
            
            # Calculate sum of slice using prefix sums
            total = prime_sums[i + length] - prime_sums[i]
            
            # Optimization: If the sum exceeds the limit, shifting the window 
            # to the right (larger primes) will only increase the sum. So we break.
            if total >= limit:
                break
            
            # Check if the sum is a prime number
            if is_prime[total]:
                print(f"Found the prime: {total}")
                print(f"Chain length: {length}")
                # Reconstruct the sequence for display (optional)
                sequence = primes[i : i + length]
                print(f"Sequence: {sequence[0]} + ... + {sequence[-1]}")
                return

if __name__ == "__main__":
    solve_consecutive_prime_sum()