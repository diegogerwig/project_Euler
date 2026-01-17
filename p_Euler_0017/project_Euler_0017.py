"""
Project Euler Problem 17: Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

def solve_number_letter_counts():
    # 1. Define the building blocks of number words
    # We use empty strings '' for index 0 to align index with the number value.
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen"]
            
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def num_to_text(n):
        """
        Converts an integer n (1 <= n <= 1000) to its English word representation.
        Returns the string without spaces or hyphens to make counting easier.
        """
        if n == 1000:
            return "onethousand"
        
        text = ""
        
        # Handle the Hundreds place (100, 200... 900)
        if n >= 100:
            # e.g., 342 // 100 = 3 ("three")
            text += ones[n // 100] + "hundred"
            
            # If there is a remainder, we must add "and" (British usage)
            if n % 100 != 0:
                text += "and"
        
        # Handle the remainder (last two digits)
        rem = n % 100
        
        if rem > 0:
            if rem < 20:
                # Direct mapping for 1-19
                text += ones[rem]
            else:
                # 20-99: Tens part + Ones part
                # e.g., 42 -> tens[4] ("forty") + ones[2] ("two")
                text += tens[rem // 10] + ones[rem % 10]
                
        return text

    # 2. Main Loop
    total_letters = 0
    
    for i in range(1, 1001):
        word = num_to_text(i)
        total_letters += len(word)
        
        # Debug print for sanity check (optional)
        # if i == 342: print(f"{i}: {word} ({len(word)})")
        # if i == 115: print(f"{i}: {word} ({len(word)})")

    print(f"Total letters used from 1 to 1000: {total_letters}")

if __name__ == "__main__":
    solve_number_letter_counts()