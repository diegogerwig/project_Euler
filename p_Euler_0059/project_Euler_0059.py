"""
Project Euler Problem 59: XOR Decryption

Decrypt the file p059_cipher.txt using a 3-letter lowercase key.
Find the sum of the ASCII values in the original text.
"""

import urllib.request
import os
import itertools

def solve_xor_decryption():
    # 1. Download/Read the file
    filename = 'p059_cipher.txt'
    url = 'https://projecteuler.net/project/resources/p059_cipher.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    with open(filename, 'r') as f:
        # File contains "79,59,12,..." -> Convert to list of ints
        cipher_text = list(map(int, f.read().strip().split(',')))
    
    # 2. Brute Force the Key
    # ASCII for 'a' is 97, 'z' is 122
    # We use itertools to generate all combinations (aaa, aab, ... zzz)
    ascii_range = range(97, 123)
    
    print("Brute forcing keys...")
    
    for key in itertools.product(ascii_range, repeat=3):
        
        # 3. Decrypt a sample to check validity
        # We don't need to decrypt the whole file to know if the key is right.
        # Decrypting the first 20-30 chars is enough to see if it's English.
        
        sample_decrypted = []
        for i, char_code in enumerate(cipher_text[:30]):
            # Cycle the key: key[0], key[1], key[2], key[0]...
            key_byte = key[i % 3]
            decrypted_char = char_code ^ key_byte # XOR operation
            sample_decrypted.append(chr(decrypted_char))
            
        sample_string = "".join(sample_decrypted)
        
        # 4. Heuristic Check
        # Does it look like English? A strong indicator is the word " the " 
        # (with spaces) or common words.
        if " the " in sample_string or "The " in sample_string:
            print(f"Key found: {tuple(chr(k) for k in key)}")
            print(f"Sample text: {sample_string}...")
            
            # 5. Full Decryption and Sum
            full_sum = 0
            full_text = []
            
            for i, char_code in enumerate(cipher_text):
                decrypted_val = char_code ^ key[i % 3]
                full_sum += decrypted_val
                full_text.append(chr(decrypted_val))
            
            print("-" * 30)
            print(f"Full Text Snippet: {''.join(full_text[:100])}...")
            print("-" * 30)
            print(f"Sum of ASCII values: {full_sum}")
            return

if __name__ == "__main__":
    solve_xor_decryption()