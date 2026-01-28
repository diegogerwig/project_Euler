"""
Project Euler Problem 72: Counting Fractions

Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?

Solution: Sum of Euler's Totient function phi(d) for 2 <= d <= 1,000,000.
"""

def solve_counting_fractions():
    limit = 1000000
    
    # Initialize phi array
    # phi[i] initially equals i
    phi = list(range(limit + 1))
    
    # Use a Sieve-like approach to calculate phi for all numbers at once
    for i in range(2, limit + 1):
        # If phi[i] is still i, it means i is prime (hasn't been reduced yet)
        if phi[i] == i:
            # Update all multiples of i (including i itself)
            # The formula for phi is n * product(1 - 1/p) for all prime factors p.
            # Here we subtract the (1/p) portion.
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
                
    # The answer is the sum of phi(d) for d from 2 to 1,000,000
    # Note: d=1 is not included because n < d implies n < 1 (no positive integer n)
    result = sum(phi[2:])
    
    print(f"Total reduced proper fractions for d <= {limit}: {result}")

if __name__ == "__main__":
    solve_counting_fractions()