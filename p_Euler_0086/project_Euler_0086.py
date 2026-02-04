"""
Project Euler Problem 86: Cuboid Route

Find the least value of M such that the number of integer shortest path solutions 
for cuboids up to M by M by M first exceeds one million.

Shortest path squared L^2 = a^2 + (b+c)^2 where a >= b >= c.
Let x = b+c. We iterate 'a' (which is M) and check x from 2 to 2a.
"""

import math

def solve_cuboid_route():
    limit_solutions = 1000000
    total_solutions = 0
    M = 0
    
    while total_solutions <= limit_solutions:
        M += 1
        a = M
        
        # We need to find pairs (b,c) such that b+c = x
        # and a^2 + x^2 is a perfect square.
        # Range of x: 2 <= x <= 2*a
        
        # Iterating x from 2 to 2*a
        for x in range(2, 2 * a + 1):
            path_sq = a * a + x * x
            path = math.isqrt(path_sq)
            
            if path * path == path_sq:
                # It is an integer path!
                # Now count valid (b,c) pairs such that b+c=x and 1 <= c <= b <= a
                
                if x <= a:
                    # c goes from 1 to x/2
                    count = x // 2
                else:
                    # x > a
                    # Constraints:
                    # b <= a  =>  x-c <= a  =>  c >= x-a
                    # c <= b  =>  c <= x/2
                    # So c ranges from (x-a) to floor(x/2)
                    count = (x // 2) - (x - a) + 1
                
                total_solutions += count

    print(f"Least value of M where solutions > {limit_solutions}: {M}")
    print(f"Total solutions found: {total_solutions}")

if __name__ == "__main__":
    solve_cuboid_route()