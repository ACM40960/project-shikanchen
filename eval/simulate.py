import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../src')
from game import Game


def simulate_games(q_table_filename, num_games=1000):
    wins = 0
    draws = 0
    losses = 0

    for _ in range(num_games):
        game = Game(q_table_filename=q_table_filename)
        game.start_new_game()

        while not game.game_over:
            # AI chooses actions based on the current visible hand values
            state = game.get_hand_visible_values()
            action = game.ai_agent.choose_action(state)

            if action == 0:  # AI chooses to hit
                game.hit()
            elif action == 1:  # AI chooses to stand
                game.stand()

        # Outcome determination
        player_value, dealer_value = game.get_hand_values()
        if player_value > 21:
            losses += 1
        elif dealer_value > 21:
            wins += 1
        elif player_value > dealer_value:
            wins += 1
        elif player_value < dealer_value:
            losses += 1
        else:
            draws += 1

    return wins, draws, losses
