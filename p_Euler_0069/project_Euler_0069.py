"""
Project Euler Problem 69: Totient Maximum

Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.

Logic:
n/phi(n) is maximized when n is a product of the smallest distinct primes.
"""

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve_totient_maximum():
    limit = 1000000
    result = 1
    current_prime = 2
    
    print("Multiplying primes:")
    
    while True:
        # Check if multiplying by the next prime stays within limit
        if result * current_prime > limit:
            break
            
        result *= current_prime
        print(f" * {current_prime} = {result}")
        
        # Find next prime
        current_prime += 1
        while not is_prime(current_prime):
            current_prime += 1
            
    print("-" * 30)
    print(f"The value of n that maximizes n/phi(n) is: {result}")

if __name__ == "__main__":
    solve_totient_maximum()