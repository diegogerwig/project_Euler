
"""
Project Euler Problem 54: Poker Hands

The file poker.txt contains one-thousand random hands dealt to two players.
How many hands does Player 1 win?
"""

import urllib.request
import os
from collections import Counter

def solve_poker_hands():
    # 1. Download/Read File
    filename = 'p054_poker.txt'
    url = 'https://projecteuler.net/project/resources/p054_poker.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    with open(filename, 'r') as f:
        lines = f.readlines()

    # 2. Setup Values Map
    # Map face cards to integers for comparison
    val_map = {r: i for i, r in enumerate('23456789TJQKA', 2)}

    def get_hand_score(hand):
        """
        Parses a hand (list of strings like ['5H', 'TC']) and returns 
        a tuple (rank, [tie_breaker_values]).
        """
        # Parse values and suits
        # values are integers, suits are chars
        values = sorted([val_map[card[0]] for card in hand], reverse=True)
        suits = [card[1] for card in hand]
        
        # Check basic properties
        is_flush = len(set(suits)) == 1
        is_straight = (max(values) - min(values) == 4) and len(set(values)) == 5
        
        # Count frequencies to detect pairs, trips, quads
        # Counter gives {Value: Count}. 
        # We sort this primarily by Count (desc), secondarily by Value (desc).
        # This is CRITICAL for tie-breakers.
        # e.g., Full House 88855 -> [(8, 3), (5, 2)] -> Tie breaker list [8, 5]
        # e.g., Two Pair 88552 -> [(8, 2), (5, 2), (2, 1)] -> Tie breaker list [8, 5, 2]
        counts = Counter(values)
        sorted_counts = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        
        # Extract just the values in order of importance for the tie-breaker list
        tie_breakers = [x[0] for x in sorted_counts]
        
        # --- Hierarchy Checks ---
        
        # 9. Royal Flush (Ace-high Straight Flush)
        # 8. Straight Flush
        if is_straight and is_flush:
            return (8, values)
            
        # 7. Four of a Kind (Count pattern: 4, 1)
        if sorted_counts[0][1] == 4:
            return (7, tie_breakers)
            
        # 6. Full House (Count pattern: 3, 2)
        if sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2:
            return (6, tie_breakers)
            
        # 5. Flush
        if is_flush:
            return (5, values)
            
        # 4. Straight
        if is_straight:
            return (4, values)
            
        # 3. Three of a Kind (Count pattern: 3, 1, 1)
        if sorted_counts[0][1] == 3:
            return (3, tie_breakers)
            
        # 2. Two Pairs (Count pattern: 2, 2, 1)
        if sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
            return (2, tie_breakers)
            
        # 1. One Pair (Count pattern: 2, 1, 1, 1)
        if sorted_counts[0][1] == 2:
            return (1, tie_breakers)
            
        # 0. High Card
        return (0, values)

    # 3. Process the Games
    p1_wins = 0
    
    for line in lines:
        cards = line.strip().split(' ')
        
        # First 5 cards are Player 1, Last 5 are Player 2
        hand1 = cards[:5]
        hand2 = cards[5:]
        
        score1 = get_hand_score(hand1)
        score2 = get_hand_score(hand2)
        
        # Python tuple comparison works perfectly here:
        # It compares element 0 (Rank). If equal, compares element 1 (Tie Breaker List).
        # List comparison is also element-by-element.
        if score1 > score2:
            p1_wins += 1

    print(f"Player 1 wins: {p1_wins}")

if __name__ == "__main__":
    solve_poker_hands()