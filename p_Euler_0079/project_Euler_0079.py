"""
Project Euler Problem 79: Passcode Derivation

The file keylog.txt contains fifty successful login attempts (3 digits each).
Determine the shortest possible secret passcode.
"""

import urllib.request
import os

def solve_passcode_derivation():
    # 1. Download and read file
    filename = 'p079_keylog.txt'
    url = 'https://projecteuler.net/project/resources/p079_keylog.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    with open(filename, 'r') as f:
        logins = f.read().splitlines()

    # 2. Identify unique digits and map predecessors
    # key: digit, value: set of digits that MUST come before it
    predecessors = {}
    
    # Get all unique characters first
    unique_chars = set("".join(logins))
    for char in unique_chars:
        predecessors[char] = set()
        
    # 3. Process the logs
    for attempt in logins:
        # attempt is like "317"
        first = attempt[0]
        second = attempt[1]
        third = attempt[2]
        
        # logic: first comes before second, so 'first' is a predecessor of 'second'
        predecessors[second].add(first)
        
        # logic: second comes before third
        predecessors[third].add(second)
        
        # logic: first comes before third (transitive, but good to be explicit)
        predecessors[third].add(first)
        
    # 4. Sort based on number of predecessors
    # The first digit will have length 0 (no numbers before it)
    # The last digit will have the max length.
    
    sorted_passcode = sorted(unique_chars, key=lambda k: len(predecessors[k]))
    
    result = "".join(sorted_passcode)
    
    # Debug info to prove logic
    print("Predecessor counts:")
    for digit in sorted_passcode:
        print(f"Digit {digit}: has {len(predecessors[digit])} predecessors {predecessors[digit]}")
        
    print("-" * 30)
    print(f"Calculated Passcode: {result}")

if __name__ == "__main__":
    solve_passcode_derivation()