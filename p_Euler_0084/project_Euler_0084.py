"""
Project Euler Problem 84: Monopoly Odds

Find the three most popular squares on a Monopoly board using two 4-sided dice.
Method: Monte Carlo Simulation.
"""

import random

def solve_monopoly_odds():
    # Parameters
    dice_sides = 4
    num_turns = 2_000_000  # 2 million turns is plenty for convergence
    
    # Board definitions
    # GO=00, JAIL=10, G2J=30, C1=11, E3=24, H2=39, R1=05
    # CC = [2, 17, 33]
    # CH = [7, 22, 36]
    
    # Init state
    current_pos = 0
    doubles_count = 0
    visits = [0] * 40
    
    # Helper to find next Railway
    def get_next_r(pos):
        # Railways are at 5, 15, 25, 35
        for r in [5, 15, 25, 35]:
            if r > pos: return r
        return 5 # Wrap around to R1
        
    # Helper to find next Utility
    def get_next_u(pos):
        # Utilities are at 12, 28
        if pos < 12: return 12
        if pos < 28: return 28
        return 12 # Wrap around
    
    random.seed(42) # For reproducibility
    
    for _ in range(num_turns):
        d1 = random.randint(1, dice_sides)
        d2 = random.randint(1, dice_sides)
        
        # Handle Doubles Logic
        if d1 == d2:
            doubles_count += 1
        else:
            doubles_count = 0
            
        if doubles_count == 3:
            current_pos = 10 # Speeding to Jail
            doubles_count = 0
            visits[current_pos] += 1
            continue
            
        # Normal Move
        current_pos = (current_pos + d1 + d2) % 40
        
        # --- Handle Special Squares (The "Jump" Logic) ---
        
        # We use a loop to handle the "Back 3 squares" -> "Community Chest" edge case
        # effectively treating movement as a state machine that settles
        while True:
            # 1. Go To Jail Square
            if current_pos == 30:
                current_pos = 10
                break # Jail ends the movement logic
            
            # 2. Community Chest (2/16 move)
            elif current_pos in [2, 17, 33]:
                # 16 cards total. 1 goes to GO(0), 1 to JAIL(10), 14 do nothing.
                # Let's verify probabilities: 1/16 each.
                card = random.randint(1, 16)
                if card == 1:
                    current_pos = 0
                elif card == 2:
                    current_pos = 10
                break # CC doesn't chain further in this problem context
                
            # 3. Chance (10/16 move)
            elif current_pos in [7, 22, 36]:
                card = random.randint(1, 16)
                
                if card == 1: current_pos = 0   # GO
                elif card == 2: current_pos = 10  # JAIL
                elif card == 3: current_pos = 11  # C1
                elif card == 4: current_pos = 24  # E3
                elif card == 5: current_pos = 39  # H2
                elif card == 6: current_pos = 5   # R1
                elif card == 7 or card == 8:      # Next R
                    current_pos = get_next_r(current_pos)
                elif card == 9:                   # Next U
                    current_pos = get_next_u(current_pos)
                elif card == 10:                  # Back 3
                    current_pos = (current_pos - 3) % 40
                    # CRITICAL: If we moved back 3, we might land on something else
                    # specifically CH(36) -> 33 is CC. We must loop again to check new pos.
                    continue 
                
                # If card > 10, no movement.
                break 
            
            else:
                # Normal square, stop processing movement
                break
        
        visits[current_pos] += 1

    # Calculate results
    # Create list of (count, square_id)
    results = []
    for i, count in enumerate(visits):
        results.append((count, i))
        
    # Sort descending by count
    results.sort(key=lambda x: x[0], reverse=True)
    
    # Get top 3
    top3 = results[:3]
    
    print("Most popular squares (Square ID : % Probability):")
    for count, sq_id in top3:
        percentage = (count / num_turns) * 100
        print(f"Square {sq_id:02d}: {percentage:.2f}%")
        
    # Format modal string
    modal_string = "".join(f"{sq_id:02d}" for _, sq_id in top3)
    print("-" * 30)
    print(f"Modal String: {modal_string}")

if __name__ == "__main__":
    solve_monopoly_odds()