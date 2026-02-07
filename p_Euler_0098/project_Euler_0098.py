"""
Project Euler Problem 98: Anagramic Squares

Find the largest square number formed by any member of an anagram word pair.
Constraint: 
1. Words must be anagrams from words.txt.
2. Substitution must result in square numbers for both words.
3. Unique mapping (different letters -> different digits).
4. No leading zeros.
"""

import math
import collections
import itertools
import os
import urllib.request

def get_word_list():
    """Download and parse the words.txt file."""
    filename = 'p098_words.txt'
    url = 'https://projecteuler.net/project/resources/p098_words.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return []

    with open(filename, 'r') as f:
        content = f.read()
        # Format is "WORD","WORD","WORD"...
        words = content.replace('"', '').split(',')
    return words

def get_anagram_pairs(words):
    """Group words by sorted letters to find anagrams."""
    anagrams = collections.defaultdict(list)
    for w in words:
        key = "".join(sorted(w))
        anagrams[key].append(w)
    
    # Filter only lists with > 1 word
    pairs = []
    for key, word_list in anagrams.items():
        if len(word_list) > 1:
            # Generate all pairs within the group (usually just 2 words, but could be 3)
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    pairs.append((word_list[i], word_list[j]))
    return pairs

def solve_anagramic_squares():
    words = get_word_list()
    pairs = get_anagram_pairs(words)
    
    # Find max length to know how many squares to generate
    max_len = 0
    for w1, w2 in pairs:
        max_len = max(max_len, len(w1))
        
    # Precompute squares by length
    # Max square needed has max_len digits -> < 10^max_len
    # Sqrt limit = 10^(max_len/2)
    limit = int(10**(max_len/2 + 1))
    squares_by_len = collections.defaultdict(set)
    
    for i in range(1, limit):
        sq = i * i
        s_sq = str(sq)
        l = len(s_sq)
        squares_by_len[l].add(s_sq)
        
    max_square_found = 0
    
    # Iterate through each anagram pair
    for w1, w2 in pairs:
        length = len(w1)
        candidate_squares = squares_by_len[length]
        
        # Try to match w1 to a square sq1
        for sq1 in candidate_squares:
            
            # Construct mapping: Letter -> Digit
            mapping = {}
            used_digits = set()
            possible = True
            
            for char, digit in zip(w1, sq1):
                if char in mapping:
                    # Consistency check: if char already mapped, must match current digit
                    if mapping[char] != digit:
                        possible = False
                        break
                else:
                    # Uniqueness check: digit must not be used by another char
                    if digit in used_digits:
                        possible = False
                        break
                    mapping[char] = digit
                    used_digits.add(digit)
            
            if not possible:
                continue
                
            # Apply mapping to w2
            # Check for leading zero in w2
            if mapping[w2[0]] == '0':
                continue
                
            # Construct number for w2
            sq2_str = "".join(mapping[c] for c in w2)
            
            # Check if sq2 is a square
            if sq2_str in candidate_squares:
                val1 = int(sq1)
                val2 = int(sq2_str)
                current_max = max(val1, val2)
                
                if current_max > max_square_found:
                    max_square_found = current_max
                    # Optional debug:
                    # print(f"Pair: {w1}-{w2}, Squares: {sq1}-{sq2_str}, Max: {current_max}")

    print(f"Largest square number formed by any member of a pair: {max_square_found}")

if __name__ == "__main__":
    solve_anagramic_squares()