'''
Main function.
Runs dice game multiple times and create statistics for the results
'''

from dice_game import dice_game

NUMBER_OF_PLAYERS = 2
TARGET_SUM = 10

print(dice_game(NUMBER_OF_PLAYERS,TARGET_SUM))
