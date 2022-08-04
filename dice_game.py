'''
Runs one game where "number_of_players" players tries to get to "target_sum" sum with dice rolls.
The function "dice_game" returns the id of the winning
'''

from dice_roll import dice_roll


def dice_game(numbers_of_players=2, target_sum=10):
    ''' Let players roll dice and check who first reach target sum '''

    a_player_reached_target_sum = False
    player_sums = [0] * numbers_of_players
    winning_player_id = 0
    # print(player_sums)

    while not a_player_reached_target_sum:
        for player_id in range(numbers_of_players):
            player_sums[player_id] += dice_roll()
            if player_sums[player_id] >= target_sum:
                a_player_reached_target_sum = True
                winning_player_id = player_id
                break

        # print(player_sums)

    # print(winning_player_id)
    return winning_player_id
