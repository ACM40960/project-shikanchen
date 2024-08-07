# Blackjack-Simulation

This project is a comprehensive simulation of the game of Blackjack, designed to explore and optimize different strategies using Q-learning algorithms. It includes a detailed implementation of the game's rules as well as an AI that learns to play Blackjack through reinforcement learning techniques.

![Python Version](https://img.shields.io/badge/Python-3.9.19-blue.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8.4-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.26.4-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Environment](https://img.shields.io/badge/Environment-blackjack--env-brightgreen.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)


## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the Blackjack simulation on your local machine, follow these steps:

```bash
git clone https://github.com/ACM40960/Blackjack-Simulation.git
cd Blackjack-Simulation
conda env create -f environment.yml
conda activate blackjack-env
```

## Project Structure

```bash
Blackjack-Simulation/
│
├── ai_models/             # Trained AI models and data
│   ├── ...
├── images/                # Images and figures used or produced by the project
│   ├── ...
├── results/               # Output results and datasets
│   ├── ...
├── eval/                  # Scripts for evaluation of simulation results
│   ├── analysis_plot.py   # Script for plotting analysis results
│   └── simulate.py        # Script for running simulations
│
├── src/                   # Source files containing the main application logic
│   ├── __init__.py        # Python Package
│   ├── agent.py           # Defines the AI agent
│   ├── card.py            # Card class for handling playing cards
│   ├── deck.py            # Deck class for handling decks of cards
│   ├── game.py            # Core game logic
│   ├── gameGUI.py         # Graphical user interface for the game
│   ├── hand.py            # Hand class for handling cards in a hand
│   ├── main.py            # Entry point of the program
│   └── train.py           # Training routines for the AI
│
├── .gitignore             # Specifies intentionally untracked files to ignore
├── environment.yml        # Conda environment file
├── LICENSE                # License details
├── literature_review.pdf  # Background literature review document
└── README.md              # Project overview and instructions
```

## Usage

This section explains how to run the Blackjack simulation program and use its features effectively.

### Running the Simulation

To start a simulation, follow these steps:

1. **Activate the Environment**: Make sure the `blackjack-env` is activated:
   ```bash
   conda activate blackjack-env
   ```
2. **Run the simulation**: Execute the main script to start the simulation:
   ```bash
   python src/main.py
   ```
   You can choose the pre-trained AI model by directly modifing the `q_table_filename` parameter in the main script before running it.

   - **Gameplay**
     - **Dealer's Hand**: The dealer's initial hand will be displayed at the top with one card face down and one card face up.
     - **Player's Hand**: Your hand is displayed openly at the bottom.
   - **Options**
     - **Hit**: The dealer's initial hand will be displayed at the top with one card face down and one card face up.
     - **Stand**: Click the `Hit` button to draw another card.
     - **Restart**: Resets the game to start a new round.
     - **AI Play**: Allows the AI to play the game automatically based on the trained model.

   - **Demo**
<div align="center">
  <img src="static/demo.gif" alt="Blackjack Game Interface Demo">
</div>
    
4. **(Optional)Retrain your own model**: Customize `train.py` by adjusting the configuration settings:

   Here are the main options you can configure:
  
   - **q_table_filename**: Specifies the path to a pre-trained Q-table. Set this to `None` to start training from scratch.
   - **num_states**: Defines the size of the state space that the AI agent considers. It's a tuple representing the dimensions of the Q-table.
   - **num_actions**: The number of possible actions the AI can take in any given state.
   - **learning_rate**: Determines how much new information overrides old information. Higher values make the agent learn faster but can lead to unstable training.
   - **discount_factor**: Indicates how much future rewards are valued over immediate rewards. Closer to 1 means the agent values future rewards more highly.
   - **exploration_rate**: The probability of the agent choosing a random action over the best-known action. This helps the agent explore new actions rather than exploiting known strategies.
   
   To modify these settings, locate where the `BlackjackAI` instance in `train.py` is created and adjust the parameters accordingly. For example:
    
   ```python
   ai_agent = BlackjackAI(
       q_table_filename='ai_models/pretrained_model.npy',
       num_states=(31, 31),
       num_actions=2,
       learning_rate=0.1,
       discount_factor=0.95,
       exploration_rate=0.1
   )
