"""
Project Euler Problem 22: Names Scores

Using names.txt, a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 

Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

import urllib.request
import os

def solve_names_scores_auto():
    filename = 'p022_names.txt'
    url = 'https://projecteuler.net/project/resources/p022_names.txt'
    
    # 1. Download the file if it doesn't exist locally
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. \nDownloading from Project Euler...")
        try:
            urllib.request.urlretrieve(url, filename)
            print("Download successful.")
        except Exception as e:
            print(f"Error downloading file: {e}")
            return

    # 2. Read the file
    with open(filename, 'r') as f:
        raw_data = f.read()

    # 3. Process data: Remove quotes and split by comma
    names = raw_data.replace('"', '').split(',')
    
    # 4. Sort Alphabetically
    names.sort()
    
    total_score = 0
    
    # 5. Calculate Scores
    # enumerate(names, 1) starts counting from 1 (rank)
    for rank, name in enumerate(names, 1):
        
        # Calculate alphabetical value (A=1, B=2, ..., Z=26)
        # ord('A') is 65, so ord(char) - 64 gives the correct value.
        name_value = sum(ord(char) - 64 for char in name)
        
        # Multiply value by rank
        score = name_value * rank
        total_score += score

    print(f"Total of all name scores: {total_score}")

if __name__ == "__main__":
    solve_names_scores_auto()