# This script takes a set of outcomes corresponding to a bet builder. It calculates the lay stakes which 
# would even the profits in all outcomes. 

import random
from itertools import product
import numpy as np

# Load input options from input_options.txt
with open('input_options.txt', 'r') as f:
    lines = f.readlines()
    score_names = eval(lines[1].split('=')[1].strip())
    score_odds = eval(lines[3].split('=')[1].strip())
    bb_odds = float(lines[5].split('=')[1].strip())
    bb_stake = float(lines[7].split('=')[1].strip())
    free_bet_percentage_return = float(lines[11].split('=')[1].strip())
    # If the free bet stake is not specified or not a valid number, default to bb_stake
    try:
        free_bet_stake = float(lines[9].split('=')[1].strip())
    except (IndexError, ValueError):
        free_bet_stake = bb_stake

# Function calculating the winnings for each outcome
def winnings(score_odds, bb_odds, bb_stake, lay_stakes, free_bet_stake=bb_stake, free_bet_percentage_return=0.8):
    stake_vec = np.array(lay_stakes+[bb_stake])
    # Create a matrix with all ones except the diagonal which is 1- the odds and the last column which is bb_odds-1
    odds_matrix = np.ones((len(stake_vec), len(stake_vec)))
    np.fill_diagonal(odds_matrix[:-1,:-1], 1-np.array(score_odds))
    odds_matrix[:-1,-1] = bb_odds-1
    # Percentage of bb stake returned as free bet if the back bet loses
    alpha = free_bet_stake / bb_stake
    odds_matrix[-1,-1] = free_bet_percentage_return*alpha -1
    profit = np.matmul(odds_matrix, stake_vec)
    return profit

# Find the optimal lay stakes which maximises the minimum profit across all outcomes
def find_optimal_lay_stakes(score_odds, bb_odds, bb_stake, free_bet_stake=bb_stake, free_bet_percentage_return=0.8):
    best_lay_stakes = None
    best_lock_in = -float('inf')
    for _ in range(10000):
        # Randomly generate lay stakes between 0 and 2 times the back stake
        lay_stakes = [random.uniform(0, bb_stake) for _ in score_odds]
        profit = winnings(score_odds, bb_odds, bb_stake, lay_stakes, free_bet_stake, free_bet_percentage_return)
        print(profit)
        lock_in = min(profit)
        if lock_in > best_lock_in:
            best_lock_in = lock_in
            best_lay_stakes = lay_stakes
    return best_lay_stakes, best_lock_in
    


if __name__ == "__main__":
    optimal_lay_stakes, optimal_lock_in = find_optimal_lay_stakes(score_odds, bb_odds, bb_stake, free_bet_stake, free_bet_percentage_return)
    print("Optimal Lay Stakes:", optimal_lay_stakes)
    print("Optimal Lock-in Value:", optimal_lock_in)
    # Print the profit for each outcome with the optimal lay stakes
    optimal_winnings_dict = winnings(score_odds, bb_odds, bb_stake, optimal_lay_stakes)
    print("Winnings for each outcome with optimal lay stakes:", optimal_winnings_dict)

