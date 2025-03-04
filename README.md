# BattleShips 

[View Live Website Here](https://project3-battleships-lewisbull-4aabd5542a7c.herokuapp.com/)

- Picture Here once deployment complete

## About

This is a classic command line battleships game, It is for One Player to try and play and beat the AI

This classic game is played on a number of various grid sizes that the player can choose, allowing for more options and varing levels of difficulty. The user selects the column and row that they want to attack and a hit or a miss marker appears on the Computers board.

The Objective is simple, sink all of the CPUs ships before they sink all of yours, but be warned, the Computer is very skilled and winning is not easy!

## Project Goals

### User Goals
- Play a fun single player game
- Have access to a leaderboard of the 10 best scores and players
- Have clear instructions on how to play the game
- Be able to have my score on the leaderboard and have the leaderboard update in real time 

### Site Owner Goals
- Create a fun and enjoyable single player game
- Give clear and easy to read instructions for the player
- Be able to add a score to a leaderboard for the player to see
- Allow the player to see a list of the 10 best scores on the leaderboard

## User Experience

### Target Audience

My target audience are people aged 7+, who has a love for games and a particular interest in retro arcade games

### User Requirements and Expectations

- A fun and enjoyable game
- A Retro arcade style
- Straight forward instructions
- A leaderboard that updates when the positions change

### User Stories
 1. As a user, I would like to know how to play the game
 2. As a user, I would like the game to be replayable in the terminal
 3. As a User, I would like to have a unique username on the leaderboard
 4. As a User, I would like to see a leaderboard of the 10 best players
 5. As a User, I would like it to be clear when I hit an enemy and when I miss
 6. As a User, I would like it to be clear how many more hits I need to win
 7. As a User, I would like for there to be a main menu

### Site Owner Stories
8. As a site owner, I would like the game to be fun and enjoyable
9. As a site owner, I would like the game to be challenging and have varying degrees of challenge
10. As a site owner, I would like the game to feel like an arcade game
11. As a site owner, I would like a leaderboard and for the users to be able to see the leaderboard
12. As a site owner, I would like the game to be consistant in design

Battleships is a Python Terminal Game, which runs in the Visual Studio Code terminal

Users can try and find all of the ships that are randomly generated by the computer,

How to play:

The user can select a row amount and column amount to between 3 and 12 rows/columns to decide the size of board, The play can make guesses on where the enemy ships are using the hits are indicated by an '*' and misses are indicated by a 'X'. The play has 40 turns to guess all of the spaces on the board to find all of the opponants battleships,

Features

Game Setup
Board Size Input:

Prompts the user to input the number of rows (row_size) and columns (col_size) for the game board.
Ensures the input values are within the valid range (3 to 12).
Validates the input to ensure it is an integer.
Game Configuration:

Defines the number of ships (num_ships), maximum and minimum ship sizes (max_ship_size and min_ship_size), and the number of turns (num_turns).
Game Boards
Internal Board Representation (board):

A 2D list representing the actual state of the game board, with ship placements marked.
Initialized with zeros to indicate empty spaces.
Player’s View Board (board_display):

A 2D list representing what the player sees, initialized with "O" to indicate unknown squares.
Updated with "X" for hits and "*" for misses.
Ship Placement
Ship Class:

Attributes:
size: The size of the ship.
orientation: The orientation of the ship (horizontal or vertical).
coordinates: The list of coordinates the ship occupies on the board.
Methods:
__init__(): Initializes a ship with given size, orientation, and location. Validates the location and orientation.
filled(): Checks if the ship's intended coordinates are already occupied on the board.
fillBoard(): Marks the ship's coordinates on the board.
contains(): Checks if a specific location is part of the ship.
destroyed(): Checks if all parts of the ship have been hit.
Random Ship Placement:

search_locations(size, orientation): Finds all valid positions on the board for a ship of a given size and orientation.
random_location(): Generates random ship attributes (size and orientation) and finds a valid position on the board using search_locations.
Game Play
Print Board:

print_board(board_array): Prints the game board in a human-readable format, displaying row and column numbers for easy reference.
Player Turn Handling:

get_row() and get_col(): Prompt the player for row and column guesses, ensuring valid inputs within the board's range.
Validates player guesses to ensure they haven't been guessed before.
Hit or Miss Detection:

Checks if the player's guess hits any ship by comparing the guess coordinates with the coordinates of each ship.
Updates the board_display with "X" for hits and "*" for misses.
If a ship is hit, checks if it is completely destroyed.
Ship Destruction:

When a ship is hit, the destroyed() method checks if all its coordinates have been hit.
If destroyed, the ship is removed from the ship_list.


Future Features
1. Enhanced AI Opponent
Smart Guessing: Implement an AI opponent that uses strategies for guessing ship locations, such as targeting nearby cells after a hit.
Difficulty Levels: Introduce different difficulty levels (easy, medium, hard) where the AI's guessing strategy and accuracy improve with higher difficulty.
2. Advanced Ship Placement
Custom Ship Layouts: Allow players to manually place their ships on the board instead of random placement, giving more control over their strategy.
Non-rectangular Ships: Introduce ships with different shapes (e.g., L-shaped, T-shaped) to add complexity and variety to the game.
3. Multiplayer Mode
Online Multiplayer: Enable players to play against each other online, with a server to manage game sessions and player turns.
Local Multiplayer: Support a local two-player mode where players take turns on the same device, with screen hiding for secret ship placement.

Data Model
Game Settings and Variables:

row_size and col_size: Dimensions of the game board, chosen by the user (between 3 and 12).
num_ships: Number of ships to be placed on the board (set to 4).
max_ship_size and min_ship_size: Maximum and minimum sizes of the ships (set to 5 and 2, respectively).
num_turns: Number of turns allowed in the game (set to 40).
Game Boards:

board: A 2D list (matrix) representing the game board with ship placements, initialized with zeros.
board_display: A 2D list representing the player's view of the board, initialized with "O" (indicating unknown squares).
Ship Class:

Ship: A class to represent each ship in the game. Each ship has:
size: Size of the ship.
orientation: Orientation of the ship ('horizontal' or 'vertical').
coordinates: List of coordinates occupied by the ship on the board.
Methods:
__init__(): Initializes the ship with size, orientation, and location.
filled(): Checks if the ship's coordinates are already occupied on the board.
fillBoard(): Marks the ship's coordinates on the board.
contains(): Checks if a given location is part of the ship.
destroyed(): Checks if the ship is completely destroyed.
Functions:

print_board(board_array): Prints the board in a readable format.
search_locations(size, orientation): Finds possible locations for a ship of given size and orientation.
random_location(): Generates a random size and orientation for a ship and finds a valid location for it.
get_row() and get_col(): Get and validate row and column guesses from the player.
Game Loop:

Ship placement: Randomly places ships on the board ensuring no overlap.
Player turns: Allows the player to make guesses to find and sink the ships, updating the board_display based on hits or misses.
End of game: Determines if the player wins (all ships sunk) or loses (turns run out with remaining ships).

Testing:

 - Did testing in the Visual Studio terminal - No issues
 - Passed through a PEP8 linter and confired no issues

Bugs
 - While I was making this code I ran into an index error, I fixed this by adding a -1 to the index.
 - Fixed an Issue where the break didnt work at the start of the loop as it was incorrect indented.

Deployed on Github

Credtis - https://www.youtube.com/@KnowledgeMavens - Credit to this youtuber for help with the python

