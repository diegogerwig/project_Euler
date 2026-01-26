"""
Project Euler Problem 61: Cyclical Figurate Numbers

Find the sum of the only ordered set of six cyclic 4-digit numbers 
for which each polygonal type (3 to 8) is represented.
"""

def get_polygonal_numbers():
    """Generates a dictionary of 4-digit polygonal numbers keyed by type."""
    # Formulas from the problem description
    formulas = {
        3: lambda n: n * (n + 1) // 2,
        4: lambda n: n * n,
        5: lambda n: n * (3 * n - 1) // 2,
        6: lambda n: n * (2 * n - 1),
        7: lambda n: n * (5 * n - 3) // 2,
        8: lambda n: n * (3 * n - 2)
    }
    
    polygons = {}
    
    for p_type, func in formulas.items():
        polygons[p_type] = []
        n = 1
        while True:
            val = func(n)
            if val >= 10000:
                break
            if val >= 1000:
                # Filter out numbers where the 3rd digit is 0 (e.g., 1209)
                # because the next number would have to start with "09", 
                # which is not a 4-digit number.
                if val % 100 >= 10:
                    polygons[p_type].append(val)
            n += 1
            
    return polygons

def solve_cyclical_figurate_numbers():
    polygons = get_polygonal_numbers()
    
    # We use recursion (Depth First Search) to find the chain.
    # chain: list of numbers currently in the cycle
    # types_used: set of polygon types (3, 4, etc.) already in the chain
    
    def find_cycle(chain, types_used):
        # Base Case: If we have 6 numbers
        if len(chain) == 6:
            # Check if the cycle closes:
            # Last 2 digits of the last number == First 2 digits of the first number
            if chain[-1] % 100 == chain[0] // 100:
                return chain
            return None

        # Recursive Step
        last_num = chain[-1]
        needed_prefix = last_num % 100
        
        # Iterate through unused types
        for p_type in range(3, 9):
            if p_type not in types_used:
                # Find candidates in this type that start with 'needed_prefix'
                for candidate in polygons[p_type]:
                    # Check prefix
                    if candidate // 100 == needed_prefix:
                        
                        # Optimization: Avoid duplicates if numbers appear in multiple sets
                        # (though logic handles types_used, keeping distinct is good)
                        
                        # Recurse
                        res = find_cycle(chain + [candidate], types_used | {p_type})
                        if res:
                            return res
        return None

    # Start the search with Octagonal numbers (type 8)
    # Since it's a cycle, it doesn't matter where we start, 
    # and type 8 has the fewest candidates, making it the fastest starting point.
    
    for start_num in polygons[8]:
        result = find_cycle([start_num], {8})
        if result:
            print("Cyclic set found!")
            print(f"Set: {result}")
            print(f"Sum: {sum(result)}")
            return

if __name__ == "__main__":
    solve_cyclical_figurate_numbers()