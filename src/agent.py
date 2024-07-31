import numpy as np


class BlackjackAI:

    # num_states: [the player’s hand values, the dealer’s visible card values]
    def __init__(self, q_table_filename=None, num_states=(31, 31), num_actions=2, learning_rate=0.1, discount_factor=0.95,
                 exploration_rate=0.1):
        if q_table_filename is None:
            self.q_table = np.zeros(num_states + (num_actions,))
        else:
            self.load_q_table(q_table_filename)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.randint(0, 2)  # choose a random action (0: hit, 1: stand)
        else:
            return np.argmax(self.q_table[state])  # choose the best known action

    def update_q_table(self, state, action, reward, next_state, done):
        if done:
            td_target = reward
        else:
            best_next_action = np.argmax(self.q_table[next_state])
            td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]

        # Compute the Temporal Difference (TD) error
        td_delta = td_target - self.q_table[state][action]

        # Update the Q-value using the TD error
        self.q_table[state][action] += self.learning_rate * td_delta

    def save_q_table(self, filename):
        np.save(filename, self.q_table)

    def load_q_table(self, filename):
        self.q_table = np.load(filename)
