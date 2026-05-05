# This script takes a set of outcomes corresponding to a bet builder. It calculates the lay stakes which 
# would even the profits in all outcomes. 

# Input score options- Names for each score i.e 2-1, 3-0 etc.
score_names = ['2-1', '3-0']
# Input score odds
score_odds = [11, 14.5]
# Input bet builder odds
bb_odds = 4.2
# Input bet builder stakes
bb_stake = 10
# Free bet stake - default is the bb_stake
free_bet_stake = bb_stake
# Input percentage return from free bet - default is 80%, 60% is better for bb-bets
free_bet_percentage_return = 0.8

import random
from itertools import product
import numpy as np

# Starting guess for lay stakes
lay_0 = bb_stake
lay_stakes = [lay_0] * len(score_names)

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

