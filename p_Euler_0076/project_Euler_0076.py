"""
Project Euler Problem 76: Counting Summations

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

def solve_counting_summations():
    target = 100
    
    # We create an array to store the number of ways to make each sum
    # Index i represents the sum i.
    ways = [0] * (target + 1)
    
    # Base case: There is 1 way to make sum 0 (by choosing nothing)
    ways[0] = 1
    
    # We iterate through all numbers that can be part of the sum.
    # We go from 1 to 99. We exclude 100 because the problem requires 
    # "at least two positive integers". If we included 100, we would 
    # count the case "100" which is just one integer.
    for i in range(1, 100):
        # Update the ways array for all numbers that can be formed using i
        for j in range(i, target + 1):
            ways[j] += ways[j - i]
            
    print(f"Number of ways to write 100 as a sum of at least two integers: {ways[target]}")

if __name__ == "__main__":
    solve_counting_summations()