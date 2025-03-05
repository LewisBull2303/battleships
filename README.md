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
 1. As a user, I would like to know how to play the game.
 2. As a user, I would like the game to be replayable in the terminal.
 3. As a User, I would like to have a username on the leaderboard.
 4. As a User, I would like to see a leaderboard of the 10 best players.
 5. As a User, I would like it to be clear when I hit an enemy and when I miss.
 6. As a User, I would like it to be clear how many more hits I need to win.
 7. As a User, I would like for there to be a main menu.
 8. As a User, I would like it to be clear the options available to me.
 9. As a User, I would like to be able to go back to the main meny from any point in the game.
 10. As a User, I would like to be able to pick a difficulty

### Site Owner Stories
11. As a site owner, I would like the game to be fun and enjoyable.
12. As a site owner, I would like the game to be challenging and have varying degrees of challenge.
13. As a site owner, I would like the game to feel like an arcade game.
14. As a site owner, I would like a leaderboard and for the users to be able to see the leaderboard.
15. As a site owner, I would like the game to be consistant in design.
16. As a Site owner, I would like my users data to be stored in a google sheet.
17. As a site owner, I would like the user to be able to naviagate my game with ease.
18. As a site owner I would like for it to be clear how to play my game.

## Technical Design

### Flow Charts
<details>
 <summary>Main Menu</summary>

![image](https://github.com/user-attachments/assets/4529bd2f-24bb-49b5-b2a3-f3bfcfdd451b)

</details>
</br>
<details>
 <summary>Gameplay Loop Flowchart - Player</summary>

![image](https://github.com/user-attachments/assets/d74fbf42-b237-4f82-b811-7f3f485b217a)

</details>
</br>
<details>
 <summary>Gameplay Loop Flowchart - CPU</summary>

![image](https://github.com/user-attachments/assets/f8e973af-2a1d-46d3-9646-bee0e86ded1b)

</details>
</br>
<details>
 <summary>Leaderboard Upload Flowchart</summary>

![image](https://github.com/user-attachments/assets/09c51548-26fd-4c55-8cdc-15ed888c29ec)

</details>
</br>

### Wireframes:
<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/e234afe8-93da-47ff-8c03-204c4bb8db13)

</details>
</br>

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
- A fun main menu which is reminiscent of an old style arace game.
- Clearly shows the player all of the choices available to them.
- Has a flashy and bold ASCII art title to draw the player in.
- User Stories answered: 7, 8, 12, 13, 16, 17
<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/f030230d-13c5-41e9-84eb-a2a7b667d638)
![image](https://github.com/user-attachments/assets/1ddd5fea-3adf-46f2-b0bb-5b258a26256b)

</details>
</br>

### Game Rules/How to play
- Clearly displays the rules and how to play to the user.
- Allows the user to return back to the main menu whenever they wish.
- User Stories answered: 1, 9, 16, 17

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/673ee8f3-25d7-463d-85ca-1bfe125f0b4b)

</details>
</br>

### Grid Select/Difficulty Select
- Gives the user multiple options on how large they want the grid
- Allows the user to select any size they wish which all corresponds to a specific difficulty
- User Stories Answered: 8, 10, 12, 15

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/9ca4ea79-c844-4a8c-80fe-79ff63a4dbd0)
![image](https://github.com/user-attachments/assets/4649bc96-f617-4cc5-9bc2-60618a666732)
![image](https://github.com/user-attachments/assets/d06d793a-d089-48c1-83c7-f8b16210bb35)
![image](https://github.com/user-attachments/assets/9b506c08-aff4-4ce1-b4cd-777ba0cac421)
![image](https://github.com/user-attachments/assets/5ddd645b-57c2-4ee1-96d6-ac8bf26432c9)
![image](https://github.com/user-attachments/assets/79484b40-a6fa-4dbe-897f-02331f78ff25)

</details>
</br>

### Leaderboard
- Clearly displays to the user the 10 best players usernames and their individual scores
- Allows the user to return back to the home page whenever they wish
- User Stories Answered: 3, 4, 14, 15, 17

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/85f870e4-54aa-4aa7-890f-1d07e64fe587)
 
</details>
</br>

### Enter a Username
- Allows the player to enter any username that they want
- The username is stored for later use in the leaderboard
- User Stories Answered: 3

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/4535e9ea-42b9-4469-9583-a1821b2a4a55)

</details>
</br>

### Player Guessing Rows and Columns
- Allows the player to guess a row and column on the CPUs board
- Does not allow the player to guess off the board or on a space they have already guessed
- User Stories Answered: 11, 18

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/23ca2fa7-2a81-418f-be9e-f651b968e789)
![image](https://github.com/user-attachments/assets/6199906c-4ab2-4e19-a9de-cc76b3174f51)

</details>
</br>

### AI Lives Tracker
- Allows the player to see how many lives the CPU has left if they hit an enemy ship
- Updates after each hit to give an accurate reading on how many more spaces the player need to hit
- User Stories Answered: 6, 11, 13

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/048f2f97-bdfc-4767-b789-008e06bcca45)

</details>
</br>

### You Hit/Missed
- Appears if the player hits or misses an enemy ship
- Changes depending on whether the player hits or misses
- Clearly states when the player hits or misses a ship
- User Stories Answered: 5, 6, 11, 15

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/374f7aa2-1a04-45e1-aad8-513d27f690f4)
![image](https://github.com/user-attachments/assets/d45dfbcc-7bb1-483f-a324-59c1a2687330)

</details>
</br>

### CPU Hit/Missed
- Appears if the CPU hits or misses a shot
- Changes depending on if the CPU hits or misses
- Clearly States when the CPU hits or misses a ship
- User Stories Answered: 5, 6, 11, 15

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/e5ba7c22-3841-4772-a66d-5484ac311c82)
![image](https://github.com/user-attachments/assets/3f4ca9dd-20d2-43a9-bcd3-ec653a975715)

</details>
</br>

### Finished Game Screen - Win
- Pops up if the player wins the game
- Asks the player if they want to add their score to the scoreboard
- If yes the score gets uploaded to the spreadsheet and sorted to its correct location
- After it asks the player if they want to play again
- If the player selects yes then they are taken back to the home screen
- If the player selects no then the game exits out
- User Stories Answered: 2, 7, 8, 9, 13 

<details>
 <summary>Images</summary>



</details>
</br>

### Finished Game Screen - Lose
- Appears when the player loses
- Asks the player if they want to play again
- If yes then it takes the player back to the main menu
- If no then it exits out of the game#
- User Stories Answered: 2, 7, 8, 9, 13  

<details>
 <summary>Images</summary>



</details>
</br>

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

