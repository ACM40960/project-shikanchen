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
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the Blackjack simulation on your local machine, follow these steps:

```bash
git clone https://github.com/yourusername/blackjack-simulation.git
cd Blackjack-Simulation
conda env create -f environment.yml
conda activate blackjack-env
```

## Project Structure

```bash
Blackjack-Simulation/
│
├── src/            # Source files for the project
│   ├── main.py     # Entry point of the program
│   ├── card.py     # Card class
│   ├── deck.py     # Deck class
│   ├── hand.py     # Hand class
│   └── game.py     # Game logic
│
├── tests/          # Unit tests for the application
│   ├── test_card.py
│   ├── test_deck.py
│   └── test_game.py
│
├── README.md       # Project overview and instructions
├── .gitignore      # Specifies intentionally untracked files to ignore
└── environment.yml # Conda environment file
```
