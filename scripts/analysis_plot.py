import matplotlib.pyplot as plt
import numpy as np
from simulate import simulate_games
from matplotlib.ticker import LogLocator, NullFormatter, FuncFormatter


def plot_results(ep, wins, draws, losses):
    # Categories of outcomes
    categories = ['Wins', 'Draws', 'Losses']
    values = [wins, draws, losses]

    # Creating the bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=['green', 'blue', 'red'])

    # Adding title and labels
    plt.title('Blackjack Simulation Outcomes')
    plt.xlabel('Outcome')
    plt.ylabel('Number of Games')
    plt.ylim(0, max(values) + 10)  # Set y-axis limits to show all bars clearly

    # Adding value labels on top of each bar
    for i in range(len(values)):
        plt.text(i, values[i] + 3, str(values[i]), ha='center', color='black')

    plt.savefig(f'../results/wld_{ep}.png', format='png', dpi=300)  # Save the figure


def plot_performance(episodes, win_rates, loss_rates, save_path='../results/performance_plot.png'):
    plt.figure(figsize=(10, 6))
    plt.plot(episodes, win_rates, marker='o', linestyle='-', color='b', label='Win Rate')
    plt.plot(episodes, loss_rates, marker='x', linestyle='--', color='r', label='Loss Rate')
    plt.title('AI Performance Improvement Over Episodes')
    plt.xlabel('Number of Training Episodes')
    plt.ylabel('Win Rate')
    plt.grid(True, which="both", ls="--")

    ax = plt.gca()  # Get current axis
    ax.set_xscale('log')  # Apply logarithmic scale

    # Handling zero by setting a minimal non-zero value for plotting purposes
    episodes = np.array(episodes, dtype=float)
    episodes[episodes == 0] = np.min(episodes[episodes > 0]) / 10  # Adjust zero to a small non-zero value

    # Custom function to format tick labels safely
    def tick_formatter(val, pos):
        if val == 0:
            return '0'  # For base model
        return f'$10^{{{int(np.log10(val))}}}$'

    ax.xaxis.set_major_formatter(plt.FuncFormatter(tick_formatter))

    # Ticks are set at the episode values, adjusted for non-zeros
    ax.set_xticks(episodes)
    plt.savefig(save_path, format='png', dpi=300)  # Save the figure


def analysis_plot():
    num_games = 10000
    episodes = [0] + [10 ** n for n in range(1, 9)]  # 0 is for the base model
    win_rates = []
    loss_rates = []
    for ep in episodes:
        wins, draws, losses = simulate_games(f'../ai_models/ai_q_table_{ep}.npy', num_games)

        win_rate = wins / num_games
        draw_rate = draws / num_games
        loss_rate = losses / num_games

        win_rates.append(win_rate)
        loss_rates.append(loss_rate)

        print(f"Simulated {num_games} games:")
        print(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")
        print(f"Win rate: {win_rate:.2f}")
        print(f"Draw rate: {draw_rate:.2f}")
        print(f"Loss rate: {loss_rate:.2f}")

        plot_results(ep, wins, draws, losses)

    plot_performance(episodes, win_rates, loss_rates)
    plt.show()


if __name__ == "__main__":
    analysis_plot()
