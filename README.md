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

## Technical Design

### Flow Charts

Main Menu:
![image](https://github.com/user-attachments/assets/4529bd2f-24bb-49b5-b2a3-f3bfcfdd451b)

Gameplay Loop Flowchart - Player:
![image](https://github.com/user-attachments/assets/d74fbf42-b237-4f82-b811-7f3f485b217a)

Gameplay Loop Flowchart - CPU:

![image](https://github.com/user-attachments/assets/f8e973af-2a1d-46d3-9646-bee0e86ded1b)

Leaderboard Upload Flowchart:
![image](https://github.com/user-attachments/assets/09c51548-26fd-4c55-8cdc-15ed888c29ec)

### Wireframes:

![image](https://github.com/user-attachments/assets/e234afe8-93da-47ff-8c03-204c4bb8db13)


## Technologies Used:

### Languages
- Python

### Frameworjs and Tools
- [Miro](https://miro.com/) - Miro was used to make the wireframes and flowcharts.
- [Visual Studio Code](https://code.visualstudio.com/) - Visual Studio Code was used to structure, create and edit all of my code. It also helped to run the code in the local terminal.
- [Git](https://git-scm.com/) - Git was used for verison control and to push chanages to my online repo.
- [GitHub](https://github.com/) - Github was used to track and store my changes.
- [Google Cloud Platform](https://cloud.google.com/cloud-console) - Google Cloud was used to get access to my spreadsheet which contained my leaderboard.

### Libraries

#### Python Libraries
- [OS](https://docs.python.org/3/library/os.html) - OS was used to clear the terminal so it did not get clogged and so it looked better for the user.
- [Random](https://docs.python.org/3/library/random.html) - Random was used to make the AI guess random spots. It was also used to put the ships in random places.
- [Copy](https://docs.python.org/3/library/copy.html#module-copy) - Copy was used to create deepcopys for the AI so everything only needed to be initialised once.
- [Time](https://docs.python.org/3/library/time.html#module-time) - Time was used to slow the loading of the game, as if the game loads to quickly it looks and feels worse for the user.
- [Gspread](https://docs.gspread.org/en/v5.3.2/) - GSpread was used to access my spreadsheet for the leaderboard and to add in users to the leaderboard.
- [Tabulate](https://pypi.org/project/tabulate/) - Tablulate was used to print the leaderboard back to the user in a nice and clean table.
- [Colorama](https://pypi.org/project/colorama/) -  Colorama was used to add color to the terminal so the experience is more fun for the user.
- [Google Oauth Service Account](https://developers.google.com/identity/protocols/oauth2) - Google OAuth was used to authorise my access to my spreadsheet, this way no one else could access it without my key.

## Features

### Main Menu
- A fun main menu which is reminiscent of an old style arace game
- Clearly shows the player all of the choices available to them
- Has a flashy and bold ASCII art title to draw the player in
- User Stories answered: 

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

