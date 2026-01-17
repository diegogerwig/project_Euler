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
    # 1. The Raw Data (String)
    raw_data = """
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

    # 2. Convert the text into a clean List of Lists
    # We create an empty list called 'triangle'
    triangle = []
    
    # Split the raw text into lines
    lines = raw_data.strip().splitlines()

    for line in lines:
        # Split each line by spaces (e.g., "95 64" becomes ["95", "64"])
        string_numbers = line.split()
        
        # Convert each string number to an Integer
        row_numbers = []
        for s in string_numbers:
            row_numbers.append(int(s))
        
        # Add this row to our triangle
        triangle.append(row_numbers)


    # 3. The Logic (Bottom-Up)
    # We want to start at the SECOND to last row and move UP to row 0.
    total_rows = len(triangle)
    
    # Range parameters: start, stop, step
    # start: total_rows - 2 (the second to last row)
    # stop: -1 (so it includes row 0)
    # step: -1 (go backwards)
    for row_index in range(total_rows - 2, -1, -1):
        
        current_row = triangle[row_index]
        row_below = triangle[row_index + 1]
        
        # Loop through each number in the current row
        for i in range(len(current_row)):
            
            # Identify the two possible numbers below this position
            left_number_below = row_below[i]
            right_number_below = row_below[i+1]
            
            # Which one is bigger?
            if left_number_below > right_number_below:
                biggest_child = left_number_below
            else:
                biggest_child = right_number_below
            
            # Add the biggest number to the current position
            current_row[i] = current_row[i] + biggest_child

    # After the loop finishes, the very top number (row 0, item 0) holds the max sum
    print("The maximum path sum is:", triangle[0][0])

if __name__ == "__main__":
    solve_maximum_path_sum()