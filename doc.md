# Connect 4 game

This project implements the logic for a classic Connect 4 game in Python. It includes player management through an Enum and a core game engine to handle board state and win conditions.

## Connect 4 Class

The `Connect4` class is the primary engine for the game. It handles the 6x7 grid, manages turns, and validates moves.

### Attributes
- `board`: A 2D list (6 rows by 7 columns). Empty cells are represented by `0`, while occupied cells contain a `Status` Enum member.
- `current_player`: Tracks whose turn it is (`Status.YELLOW` or `Status.RED`).

### Methods

#### `__init__()`
Initializes a new game with an empty board and sets the first player to Yellow.

#### `drop(column: int) -> bool`
Places the current player's piece into the specified column (0-6).
- The piece automatically occupies the lowest available row.
- If successful, it toggles the `current_player` and returns `True`.
- If the column is full, it returns `False`.

#### `isFinished() -> bool`
Scans the entire board to determine if a player has achieved four in a row.
- Checks **Horizontal** (→), **Vertical** (↓), and both **Diagonal** (↘ and ↙) directions.
- Returns `True` if a win condition is met.

#### `isComplete() -> bool`
Checks if the game board is completely full (a draw state). It verifies if any cells in the top row are still `0`.

#### `play()`
A CLI-based game loop that prints the board and accepts user input via the terminal until the game concludes.

---

## Status Enum

The `Status` enumeration defines the players and potential observers in the game.

### Members
- `YELLOW`: Represents the first player (Value: 1).
- `RED`: Represents the second player (Value: 2).
- `SPECTATOR`: Represents an observer (Value: 3).

### Methods

#### `invert()`
A helper method to switch between active players. Returns `RED` if called on `YELLOW`, and vice versa.

#### `__str__()`
Returns the string representation used in the board display ("1" or "2").

---

## Getting Started
To start a game from the command line, simply run the script directly:
```python
python Connect4.py
```