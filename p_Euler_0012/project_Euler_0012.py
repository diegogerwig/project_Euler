#!/usr/bin/python3

"""
Highly Divisible Triangular Number

Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th
triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
1  : 1
3  : 1, 3
6  : 1, 2, 3, 6
10 : 1, 2, 5, 10
15 : 1, 3, 5, 15
21 : 1, 3, 7, 21
28 : 1, 2, 4, 7, 14, 28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import math
from typing import Tuple


def triangle_number(n: int) -> int:
    """
    Calculate the nth triangle number.
    
    Formula: T(n) = n * (n + 1) / 2
    
    Args:
        n (int): Position of the triangle number
        
    Returns:
        int: The nth triangle number
        
    Example:
        >>> triangle_number(7)
        28
    """
    return n * (n + 1) // 2


def count_divisors(n: int) -> int:
    """
    Count the number of divisors of a given number.
    
    Optimization: We only need to check up to the square root of n.
    
    Args:
        n (int): Number to count divisors for
        
    Returns:
        int: Number of divisors
        
    Example:
        >>> count_divisors(28)
        6
    """
    if n <= 0:
        return 0
    
    count = 0
    sqrt_n = int(math.sqrt(n))
    
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 1
            # If i is not the exact square root, also count n/i
            if i != n // i:
                count += 1
                
    return count


def count_divisors_optimized(n: int) -> int:
    """
    Optimized version to count divisors using prime factorization.
    
    If n = p1^a1 * p2^a2 * ... * pk^ak, then
    number of divisors = (a1+1) * (a2+1) * ... * (ak+1)
    
    Args:
        n (int): Number to count divisors for
        
    Returns:
        int: Number of divisors
    """
    if n <= 0:
        return 0
    
    divisors = 1
    temp = n
    
    # Count factors of 2
    count = 0
    while temp % 2 == 0:
        temp //= 2
        count += 1
    if count > 0:
        divisors *= (count + 1)
    
    # Count odd factors
    i = 3
    while i * i <= temp:
        count = 0
        while temp % i == 0:
            temp //= i
            count += 1
        if count > 0:
            divisors *= (count + 1)
        i += 2
    
    # If temp > 1, then it's a prime factor
    if temp > 1:
        divisors *= 2
        
    return divisors


def find_triangle_with_divisors(target_divisors: int, use_optimized: bool = True) -> Tuple[int, int, int]:
    """
    Find the first triangle number with more than 'target_divisors' divisors.
    
    Args:
        target_divisors (int): Minimum number of divisors required
        use_optimized (bool): Whether to use the optimized version for counting divisors
        
    Returns:
        Tuple[int, int, int]: (position, triangle number, number of divisors)
        
    Example:
        >>> find_triangle_with_divisors(5)
        (7, 28, 6)
    """
    count_func = count_divisors_optimized if use_optimized else count_divisors
    
    n = 1
    while True:
        triangle = triangle_number(n)
        divisor_count = count_func(triangle)
        
        if divisor_count > target_divisors:
            return n, triangle, divisor_count
            
        n += 1


def verify_examples():
    """
    Verify the examples given in the problem.
    """
    print("Verifying problem examples:")
    print("=" * 40)
    
    # Verify the first triangle numbers
    expected_triangles = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    print("First 10 triangle numbers:")
    for i in range(1, 11):
        triangle = triangle_number(i)
        print(f"T({i}) = {triangle}", end="")
        if triangle == expected_triangles[i-1]:
            print(" ✓")
        else:
            print(f" ✗ (expected: {expected_triangles[i-1]})")
    
    print("\nFactors of the first 7 triangle numbers:")
    expected_divisors = [1, 2, 4, 4, 4, 4, 6]
    
    for i in range(1, 8):
        triangle = triangle_number(i)
        divisors = count_divisors(triangle)
        print(f"{triangle:2d} has {divisors} divisors", end="")
        if divisors == expected_divisors[i-1]:
            print(" ✓")
        else:
            print(f" ✗ (expected: {expected_divisors[i-1]})")


def main():
    """
    Main function that solves the problem.
    """
    print("PROBLEM 12: Highly Divisible Triangular Number")
    print("=" * 50)
    
    # Verify examples
    verify_examples()
    
    print(f"\nFinding the first triangle number with more than 5 divisors:")
    pos, triangle, divisors = find_triangle_with_divisors(5)
    print(f"Result: T({pos}) = {triangle} has {divisors} divisors")
    
    print(f"\nFinding the first triangle number with more than 500 divisors:")
    print("(This may take a few seconds...)")
    
    pos, triangle, divisors = find_triangle_with_divisors(500)
    print(f"Result: T({pos}) = {triangle} has {divisors} divisors")
    
    print(f"\nANSWER: {triangle}")


if __name__ == "__main__":
    main()