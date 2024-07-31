from game import Game
from agent import BlackjackAI


class BlackjackEnvironment:
    def __init__(self):
        self.game = Game()

    def reset(self):
        self.game.start_new_game()
        return self.game.get_hand_visible_values()

    def step(self, action):
        if action == 0:
            self.game.hit()
            next_state = self.game.get_hand_visible_values()
        elif action == 1:
            self.game.stand()
            next_state = self.game.get_hand_values()

        reward = self.game.calculate_reward()
        return next_state, reward, self.game.game_over


def train_ai(episodes=100000):
    env = BlackjackEnvironment()
    ai_agent = BlackjackAI()

    for episode in range(episodes):
        state = env.reset()
        total_reward = 0

        while True:
            action = ai_agent.choose_action(state)
            next_state, reward, done = env.step(action)
            ai_agent.update_q_table(state, action, reward, next_state, done)

            state = next_state
            total_reward += reward

            if done:
                break

        if episode % 100 == 0:
            print(f"Episode: {episode}, Total Reward: {total_reward}")

    ai_agent.save_q_table(f"../ai_models/ai_q_table_{episodes}.npy")


if __name__ == "__main__":
    counter = 100000
    while counter <= 100000000:
        train_ai(episodes=counter)
        counter *= 10
