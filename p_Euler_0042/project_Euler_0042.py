"""
Project Euler Problem 42: Coded Triangle Numbers

The nth term of the sequence of triangle numbers is given by tn = 0.5*n*(n+1).
By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values we form a word value.

Using words.txt, how many are triangle words?
"""

import urllib.request
import os

def solve_coded_triangle_numbers():
    # 1. Download and Read File
    filename = 'p042_words.txt'
    url = 'https://projecteuler.net/project/resources/p042_words.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    with open(filename, 'r') as f:
        raw_data = f.read()
        
    # Parse: Remove quotes and split by comma
    words = raw_data.replace('"', '').split(',')
    
    # 2. Pre-compute Triangle Numbers
    # What is the maximum possible word score? 
    # Even a long word like "RESPONSIBILITY" (14 chars) is < 364 (14 * 26).
    # We can safely generate triangle numbers up to a generous limit.
    triangle_numbers = set()
    n = 1
    while True:
        val = int(0.5 * n * (n + 1))
        triangle_numbers.add(val)
        n += 1
        
        # Stop if the triangle number is way larger than any possible word score
        if val > 1000:
            break
            
    # 3. Check Words
    triangle_word_count = 0
    
    for word in words:
        # Calculate word value (A=1, B=2...)
        word_value = sum(ord(char) - 64 for char in word)
        
        if word_value in triangle_numbers:
            triangle_word_count += 1
            
    print(f"Total words processed: {len(words)}")
    print(f"Number of triangle words: {triangle_word_count}")

if __name__ == "__main__":
    solve_coded_triangle_numbers()