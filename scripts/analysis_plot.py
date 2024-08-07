import matplotlib.pyplot as plt
from simulate import simulate_games
from matplotlib.ticker import ScalarFormatter


def plot_results(wins, draws, losses):
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

    # Show the plot
    plt.show()


def plot_performance(episodes, win_rates):
    plt.figure(figsize=(10, 6))
    plt.plot(episodes, win_rates, marker='o', linestyle='-', color='b')
    plt.title('AI Performance Improvement Over Episodes')
    plt.xlabel('Number of Training Episodes')
    plt.ylabel('Win Rate')
    plt.grid(True)

    # Set the x-axis to scientific notation
    ax = plt.gca()  # Get the current Axes instance
    formatter = ScalarFormatter(useMathText=True)  # Create formatter
    formatter.set_scientific(True)  # Enable scientific notation
    formatter.set_powerlimits((-1, 1))  # Use scientific notation if log10 of the axis range is outside -1 to 1
    ax.xaxis.set_major_formatter(formatter)  # Apply the formatter to the x-axis

    plt.xticks(episodes, [f"${int(ep):.1e}$" for ep in episodes])  # Formatting ticks as scientific notation
    plt.show()


def analysis_plot():
    num_games = 1000
    episodes = [0] + [10**n for n in range(1, 9)]  # 0 is for the base model
    win_rates = []
    for ep in episodes:
        wins, draws, losses = simulate_games(f'../ai_models/ai_q_table_{ep}.npy', num_games)

        win_rate = wins / num_games
        draw_rate = draws / num_games
        loss_rate = losses / num_games

        win_rates.append(win_rate)

        print(f"Simulated {num_games} games:")
        print(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")
        print(f"Win rate: {win_rate:.2f}")
        print(f"Draw rate: {draw_rate:.2f}")
        print(f"Loss rate: {loss_rate:.2f}")

        plot_results(wins, draws, losses)

    plot_performance(episodes, win_rates)


if __name__ == "__main__":
    analysis_plot()
