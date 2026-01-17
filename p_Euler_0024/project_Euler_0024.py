"""
Project Euler Problem 24: Lexicographic Permutations

A permutation is an ordered arrangement of objects. 
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools

def solve_lexicographic_permutations():
    # 1. Define the digits to be permuted
    # Ideally, they should be sorted to ensure lexicographic order starts correctly.
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # 2. Define the target index
    # The problem asks for the 1,000,000th permutation.
    # Since Python lists are 0-indexed, we look for index 999,999.
    target_index = 1000000 - 1
    
    # 3. Generate permutations
    # itertools.permutations(iterable) returns an iterator yielding 
    # tuples of elements in lexicographic order (if input is sorted).
    # 
    # Note: There are 10! (3,628,800) total permutations. 
    # Generating them all takes less than a second in Python.
    permutations_iterator = itertools.permutations(digits)
    
    # 4. Extract the specific permutation
    # We can use 'next(islice(...))' for efficiency to avoid creating a full list,
    # or simpler: just create the list and access the index since 3M items fits in memory.
    
    # Efficient way using islice (consumes iterator up to target):
    from itertools import islice
    result_tuple = next(islice(permutations_iterator, target_index, None))
    
    # 5. Format the result
    # The result is a tuple like (2, 7, 8, ...). We need to join it into a string.
    result_string = "".join(str(d) for d in result_tuple)
    
    print(f"The {target_index + 1}th lexicographic permutation is: {result_string}")

if __name__ == "__main__":
    solve_lexicographic_permutations()