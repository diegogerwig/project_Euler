"""
Project Euler Problem 32: Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the digits 
1 to n exactly once.
The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.
"""

def solve_pandigital_products():
    # Use a set to store products because the problem hint says:
    # "Some products can be obtained in more than one way so be sure to only include it once"
    pandigital_products = set()
    
    # We check combinations of a * b = product
    # Logic for limits:
    # 1-digit * 4-digits = 4-digits (Total 9) -> a in range(1, 10), b in range(1000, 10000)
    # 2-digits * 3-digits = 4-digits (Total 9) -> a in range(10, 100), b in range(100, 1000)
    
    # To simplify, we can iterate 'a' from 2 up to ~100.
    # We iterate 'b' starting from 'a + 1' to avoid duplicate checks (commutative property)
    # and go up to roughly 2000 (enough to cover the 4-digit requirement).
    
    for a in range(2, 100):
        # Determine starting point for b. 
        # If a is 1-digit, b starts at 1234
        # If a is 2-digit, b starts at 123
        start_b = 123 if a > 9 else 1234
        
        # Upper limit for b is not strict, we break when product is too large
        for b in range(start_b, 10000):
            
            product = a * b
            
            # Combine all numbers into one string
            full_str = str(a) + str(b) + str(product)
            
            # Optimization: If length is > 9, we stop this inner loop immediately
            # because increasing b will only make the string longer.
            if len(full_str) > 9:
                break
            
            # If length is exactly 9, check if it contains digits 1-9
            if len(full_str) == 9:
                # Sorting the string is an easy way to check if it equals "123456789"
                if "".join(sorted(full_str)) == "123456789":
                    pandigital_products.add(product)
                    # print(f"Found: {a} x {b} = {product}")

    total_sum = sum(pandigital_products)
    
    print(f"Unique products found: {pandigital_products}")
    print(f"Sum of products: {total_sum}")

if __name__ == "__main__":
    solve_pandigital_products()