# Pacman Game with AI

A Pacman game implementation with an AI player using the Minimax algorithm. This project showcases the classic Pacman game environment, where the player (Pacman) navigates a maze to collect points while avoiding ghosts. The AI-controlled ghosts aim to catch Pacman.

## Table of Contents

- [Introduction](#introduction)
- [Game Features](#game-features)
- [Implemented Classes](#implemented-classes)
- [How to Play](#how-to-play)
- [AI Algorithm - Minimax](#ai-algorithm---minimax)
- [Project Structure](#project-structure)
- [Running the Game](#running-the-game)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project provides a Python implementation of a Pacman game with an AI-controlled Pacman. The game board is randomly generated, and the player's goal is to collect points while avoiding ghosts. The AI-controlled ghosts move randomly, and the game ends if Pacman is caught.

## Game Features

- **Randomly Generated Board**: The game board is randomly generated with walls and points for Pacman to collect.
- **AI-Controlled Ghosts**: The ghosts move randomly on the board, creating a challenge for Pacman.
- **Score Tracking**: The game tracks the player's score, increasing for each point collected and decreasing if caught by a ghost.
- **Game Over**: The game ends if Pacman is caught by a ghost or if all points are collected.

## Implemented Classes

- **Game Class**: Manages the game state, including the board, Pacman and ghost positions, and the player's score.
- **Ghosts Class**: Controls the movement of the ghosts, either randomly or based on specified actions.
- **Pacman Class**: Implements the Minimax algorithm for Pacman's moves and evaluates the utility of different game states.
- **Play Class**: Handles the game loop, player input, and updates to the game state.
- **Utility Class**: Provides utility functions for calculating game state utilities, checking game completion, and evaluating distances.

## How to Play

The game is played in the console. Pacman's movements are controlled by the AI, and the player can observe the game state and score.

## AI Algorithm - Minimax

Pacman's movements are determined using the Minimax algorithm. The algorithm evaluates possible future game states, considering both Pacman and the ghosts, to make the optimal move that maximizes the utility of the game state.

## Project Structure

- `game.py`: Contains the main Game class for managing the game state.
- `ghosts.py`: Implements the Ghosts class for controlling ghost movements.
- `pacman.py`: Defines the Pacman class, which uses the Minimax algorithm for decision-making.
- `play.py`: Handles the game loop and user interface.
- `utility.py`: Provides utility functions for evaluating game states.

## Running the Game

To run the game, execute the `play.py` script. Ensure that Python and the required dependencies are installed.

```bash
python play.py
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

