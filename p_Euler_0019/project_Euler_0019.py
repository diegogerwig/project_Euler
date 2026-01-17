"""
Project Euler Problem 19: Counting Sundays

How many Sundays fell on the first of the month during the 
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime

def solve_counting_sundays_easy():
    sundays_count = 0
    
    # Iterate through all years in the 20th century (1901 to 2000 inclusive)
    for year in range(1901, 2001):
        
        # Iterate through all 12 months
        for month in range(1, 13):
            
            # Create a date object for the 1st of the current month
            # Format: datetime.date(year, month, day)
            current_date = datetime.date(year, month, 1)
            
            # Check the day of the week
            # In Python's datetime: Monday is 0, Tuesday is 1 ... Sunday is 6
            if current_date.weekday() == 6:
                sundays_count += 1
                
    print(f"Number of Sundays on the 1st of the month: {sundays_count}")

if __name__ == "__main__":
    solve_counting_sundays_easy()