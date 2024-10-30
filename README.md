# Turtle Crossing Game

## Overview
The **Turtle Crossing Game** is a simple game inspired by the classic arcade game "Frogger". The goal is to help the turtle cross the screen from bottom to top without colliding with any moving cars. Each successful crossing increases the game’s difficulty by speeding up the cars.

This game is implemented in Python using the `turtle` graphics library.

## How to Play
- Press the **Up Arrow key** to move the turtle upwards.
- Avoid the moving cars; if the turtle collides with any car, the game ends.
- Each time the turtle reaches the top of the screen, it will reset to the bottom, and the car speeds will increase.

## Game Structure
The code is organized into three main classes:
1. **Player**: Represents the turtle, which can move up in response to the Up Arrow key. It checks if it has reached the top of the screen and resets its position after each successful crossing.
2. **CarManager**: Manages car objects, creating new cars at random intervals and moving them from right to left across the screen. It also increases the speed of the cars as the player progresses.
3. **Scoreboard**: Manages the player's score, updating each time the turtle successfully crosses the screen. It also displays a "Game Over" message when a collision occurs.

## Code Structure
- **main.py**: Sets up the game screen, listens for player input, and contains the main game loop.
- **player.py**: Contains the `Player` class and handles turtle movements and position reset.
- **car_manager.py**: Contains the `CarManager` class, which handles car creation, movement, and speed adjustments.
- **scoreboard.py**: Contains the `Scoreboard` class, which updates and displays the score and shows the "Game Over" message.

## Requirements
- Python 3.x
- `turtle` graphics library (pre-installed with Python)

## Setup Instructions
1. Clone the repository.
2. Run `main.py` to start the game:
   ```bash
   python main.py
   ```

## Game Controls
- **Up Arrow Key**: Move the turtle forward

## Project Files
- `main.py`: Main game script
- `player.py`: Contains `Player` class
- `car_manager.py`: Contains `CarManager` class
- `scoreboard.py`: Contains `Scoreboard` class

## Future Improvements
- Add levels with varying obstacles and speeds.
- Introduce power-ups or bonuses.
- Implement multi-directional movement for the player.

---