"""
Project Euler Problem 38: Pandigital Multiples

Take the number 192 and multiply it by each of 1, 2, and 3:
192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
Concatenating each product we get the 1 to 9 pandigital, 192384576.

What is the largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def is_pandigital(s):
    """Checks if a string contains digits 1-9 exactly once."""
    if len(s) != 9:
        return False
    return sorted(s) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def solve_pandigital_multiples():
    # Based on our analysis, the candidate integer must be a 4-digit number
    # starting with 9 to maximize the result.
    # The concatenation will be formed by (integer * 1) concatenated with (integer * 2).
    
    largest_pandigital = 0
    
    # We iterate backwards from 9999 to 9000.
    # The first valid pandigital we find is guaranteed to be the largest
    # because the result starts with the integer itself.
    for i in range(9999, 9000, -1):
        
        # Form the product string
        # part1 is 4 digits, part2 is 5 digits (since 9xxx * 2 = 18xxx)
        part1 = i * 1
        part2 = i * 2
        concatenated = str(part1) + str(part2)
        
        if is_pandigital(concatenated):
            largest_pandigital = int(concatenated)
            print(f"Found max with integer: {i}")
            print(f"Calculation: {i} x 1 = {part1}, {i} x 2 = {part2}")
            print(f"Result: {concatenated}")
            break
            
    # Just in case our 4-digit theory was wrong (it isn't), 
    # we know 9 -> 918273645 is a baseline candidate.
    if largest_pandigital == 0:
        print("Fallback: 918273645")

if __name__ == "__main__":
    solve_pandigital_multiples()