"""
Project Euler Problem 31: Coin Sums

In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

How many different ways can £2 be made using any number of coins?
Target is 200p.
"""

def solve_coin_sums():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    
    # 1. Initialize the ways array
    # ways[i] will store the number of ways to make the value 'i'
    # Size is 201 because we need index 0 to index 200.
    ways = [0] * (target + 1)
    
    # Base case: There is exactly 1 way to make 0 pence (using no coins)
    ways[0] = 1
    
    # 2. Iterate through each type of coin
    for coin in coins:
        # Update the 'ways' array for every value from the coin amount up to the target
        # Logic: ways[i] = existing_ways + ways[i - coin_value]
        # This means: "Take the ways we knew without this coin, plus the ways
        # we could reach the remainder (i - coin) using this coin."
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
            
    # 3. The result is at the target index
    print(f"Target value: {target}p")
    print(f"Coins available: {coins}")
    print(f"Total different ways to make £2: {ways[target]}")

if __name__ == "__main__":
    solve_coin_sums()