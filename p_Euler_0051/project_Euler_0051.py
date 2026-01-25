"""
Project Euler Problem 51: Prime Digit Replacements

Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, 
is part of an eight prime value family.
"""

def sieve_primes(limit):
    """Generates primes and a fast lookup set up to limit."""
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False
                
    primes = [i for i, p in enumerate(is_prime) if p]
    return primes, is_prime

def get_family_size(pattern, is_prime_list):
    """
    Given a pattern like "12*3*", count how many primes are formed
    by replacing '*' with 0-9.
    """
    prime_family = []
    
    for digit in '0123456789':
        # Don't allow leading zeros
        if digit == '0' and pattern[0] == '*':
            continue
            
        # Create the number string
        num_str = pattern.replace('*', digit)
        num = int(num_str)
        
        # Check primality using our pre-calculated sieve
        if num < len(is_prime_list) and is_prime_list[num]:
            prime_family.append(num)
            
    return prime_family

def solve_prime_digit_replacements():
    # We expect the answer to be a 6-digit number based on problem difficulty
    limit = 1000000
    primes, is_prime_lookup = sieve_primes(limit)
    
    print(f"Primes generated up to {limit}. Starting search...")
    
    # Iterate through primes to find the base candidate
    for p in primes:
        s = str(p)
        
        # Heuristic: We are looking for 8-prime families.
        # This almost certainly requires replacing 3 digits (to avoid div by 3 issues).
        # The repeating digit in the smallest prime must be 0, 1, or 2.
        
        for duplicate_digit in '012':
            if s.count(duplicate_digit) == 3:
                
                # Create the pattern (mask)
                # e.g., if p=121313 and duplicate is '1', pattern="*2*3*3"
                pattern = s.replace(duplicate_digit, '*')
                
                # Check the family size for this pattern
                family = get_family_size(pattern, is_prime_lookup)
                
                if len(family) == 8:
                    print("-" * 30)
                    print(f"Solution Found!")
                    print(f"Smallest Prime: {family[0]}")
                    print(f"Family: {family}")
                    print(f"Pattern: {pattern}")
                    return

if __name__ == "__main__":
    solve_prime_digit_replacements()