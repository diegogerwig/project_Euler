"""
Project Euler Problem 18: Maximum Path Sum I

By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle provided.
"""

def solve_maximum_path_sum():
    # 1. The Input Data
    triangle_data = """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """

    # 2. Parse the data into a list of lists of integers
    # strip() removes empty start/end lines, splitlines() creates rows
    # Then we map each number in the row to an integer
    triangle = [list(map(int, line.split())) for line in triangle_data.strip().splitlines()]

    # 3. Algorithm: Bottom-Up Dynamic Programming
    # We start from the second to last row and move upwards to the top (row 0).
    # range(start, stop, step): start at len-2, stop at -1 (exclusive, so 0), step -1
    for i in range(len(triangle) - 2, -1, -1):
        
        # Iterate through every number in the current row
        for j in range(len(triangle[i])):
            
            # Compare the two numbers directly below the current number (triangle[i][j]):
            # The one directly below is at [i+1][j]
            # The one below and to the right is at [i+1][j+1]
            left_child = triangle[i+1][j]
            right_child = triangle[i+1][j+1]
            
            # Add the maximum of the two children to the current number
            triangle[i][j] += max(left_child, right_child)

    # After the loop finishes, the top element contains the maximum sum
    max_total = triangle[0][0]

    print(f"The maximum path sum is: {max_total}")

if __name__ == "__main__":
    solve_maximum_path_sum()