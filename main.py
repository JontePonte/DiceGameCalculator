'''
Main function.
Runs dice game multiple times and create statistics for the results
'''

from dice_game import dice_game

NUMBER_OF_PLAYERS = 2
TARGET_SUM = 10
NUMBER_OF_ROUNDS = 10000

player_wins = [0]*NUMBER_OF_PLAYERS


for _ in range(NUMBER_OF_ROUNDS):
    round_winner = dice_game(NUMBER_OF_PLAYERS,TARGET_SUM)

    for (player_id, _) in enumerate(player_wins):
        if round_winner == player_id:
            player_wins[player_id] += 1

win_fractions = []
_ = [win_fractions.append((i/NUMBER_OF_ROUNDS)) for i in player_wins]

print(win_fractions)
