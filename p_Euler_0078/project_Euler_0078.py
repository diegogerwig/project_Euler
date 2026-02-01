"""
Project Euler Problem 78: Coin Partitions

Find the least value of n for which p(n) is divisible by one million.
Method: Euler's Pentagonal Number Theorem (O(n*sqrt(n))).
Recurrence: p(n) = sum( (-1)^(k-1) * p(n - gk) )
where gk = k(3k-1)/2 for k = 1, -1, 2, -2...
"""

def solve_coin_partitions():
    target_mod = 1000000
    p = [1]  # p(0) = 1
    n = 1
    
    print("Searching for n where p(n) is divisible by 1,000,000...")
    
    while True:
        pn = 0
        k = 1
        
        while True:
            # Generate generalized pentagonal numbers
            # We check pairs: k and -k
            # k = 1 -> pent = 1(2)/2 = 1
            # k = -1 -> pent = -1(-4)/2 = 2
            
            # Using loop index k to generate terms for k and -k
            
            # Term for positive k
            pent1 = (k * (3 * k - 1)) // 2
            
            # Term for negative k (which simplifies to k(3k+1)/2)
            pent2 = (k * (3 * k + 1)) // 2
            
            if pent1 > n:
                break
            
            # Determine sign: 
            # k=1 (odd) -> +, k=2 (even) -> -, k=3 (odd) -> +
            if k % 2 != 0:
                sign = 1
            else:
                sign = -1
                
            pn += sign * p[n - pent1]
            
            # Check the second pentagonal number of the pair
            if pent2 <= n:
                pn += sign * p[n - pent2]
            
            # Keep numbers small
            pn %= target_mod
            
            k += 1
            
        # Store result for current n
        p.append(pn)
        
        if pn == 0:
            print(f"Solution found: n = {n}")
            print(f"p({n}) is divisible by {target_mod}")
            return
            
        n += 1

if __name__ == "__main__":
    solve_coin_partitions()