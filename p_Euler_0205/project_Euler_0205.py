"""
Project Euler Problem 205: Dice Game

Calculate the probability that Pyramidal Peter (9 four-sided dice)
beats Cubic Colin (6 six-sided dice).
"""

def get_distribution(num_dice, sides):
    """
    Returns a dictionary {sum: count} representing the frequency
    of each possible sum for a given number of dice and sides.
    """
    # Start with 0 dice having a sum of 0 with 1 way (base case)
    # distribution = {sum: count}
    dist = {0: 1}
    
    for _ in range(num_dice):
        new_dist = {}
        # Iterate over existing sums
        for current_sum, count in dist.items():
            # Add the result of the new die (1 to sides)
            for face in range(1, sides + 1):
                new_sum = current_sum + face
                if new_sum not in new_dist:
                    new_dist[new_sum] = 0
                new_dist[new_sum] += count
        dist = new_dist
        
    return dist

def solve_dice_game():
    # 1. Calculate distributions
    # Peter: 9 dice, 4 sides
    peter_dist = get_distribution(9, 4)
    
    # Colin: 6 dice, 6 sides
    colin_dist = get_distribution(6, 6)
    
    # 2. Count winning scenarios
    # Total space size
    total_peter_outcomes = 4**9
    total_colin_outcomes = 6**6
    total_combinations = total_peter_outcomes * total_colin_outcomes
    
    peter_wins_count = 0
    
    # Compare every possible sum of Peter vs Colin
    for p_sum, p_count in peter_dist.items():
        for c_sum, c_count in colin_dist.items():
            
            if p_sum > c_sum:
                # If Peter's sum is greater, add the number of ways this specific matchup can happen
                peter_wins_count += (p_count * c_count)
                
    # 3. Calculate probability
    probability = peter_wins_count / total_combinations
    
    # Output formatted to 7 decimal places
    print(f"Probability that Pyramidal Peter beats Cubic Colin: {probability:.7f}")

if __name__ == "__main__":
    solve_dice_game()