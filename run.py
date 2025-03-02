from random import randint
import copy
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleships_leaderboard')

rows = 10
cols = 10

# Setting up the Constants and variables
OCEAN = "O" # Icon for the ocean spaces
FIRE = "X" # Icon for a miss
HIT = "*" # Icon for a hit
SHIPS = [5, 4, 3, 3, 2] # Sizes of the ships
SEA = [] # Empty list for the sea (grid)

orientation = -1 # Stores the ship's hit orientation
total_hits = [] # Stores the ship number every time the bot hits a ship
miss = 1 # Stores whether the last AI shot was a miss
turns_taken = 0 #Stores the number of turns taken for the leaderboard
username = "PLACEHOLDER"

player_ship_lives = 17 # The amount of lives for the player (equal to the ships)
ship_position = [] 
ship_length = []

player_radar = [] # The radar board for the player
player_board = [] # The board representing player ships' positions
ai_radar = [] # The radar board for the AI
ai_board = [] # The board representing AI ships' positions
ai_ship_lives = 17 # The AI lives (equal to the ship parts)

def get_username():
    global username
    username = input("\nPlease enter your username: ")
    return username

# Main menu function for selecting options
def main_menu():
    while True:
        print("""
==========================================================================      
▀█████████▄     ▄████████     ███         ███      ▄█          ▄████████      
  ███    ███   ███    ███ ▀█████████▄ ▀█████████▄ ███         ███    ███      
  ███    ███   ███    ███    ▀███▀▀██    ▀███▀▀██ ███         ███    █▀       
 ▄███▄▄▄██▀    ███    ███     ███   ▀     ███   ▀ ███        ▄███▄▄▄          
▀▀███▀▀▀██▄  ▀███████████     ███         ███     ███       ▀▀███▀▀▀          
  ███    ██▄   ███    ███     ███         ███     ███         ███    █▄       
  ███    ███   ███    ███     ███         ███     ███▌    ▄   ███    ███      
▄█████████▀    ███    █▀     ▄████▀      ▄████▀   █████▄▄██   ██████████      
                                                  ▀                           
   ▄████████    ▄█    █▄     ▄█     ▄███████▄    ▄████████                    
  ███    ███   ███    ███   ███    ███    ███   ███    ███                    
  ███    █▀    ███    ███   ███▌   ███    ███   ███    █▀                     
  ███         ▄███▄▄▄▄███▄▄ ███▌   ███    ███   ███                           
▀███████████ ▀▀███▀▀▀▀███▀  ███▌ ▀█████████▀  ▀███████████                    
         ███   ███    ███   ███    ███                 ███                    
   ▄█    ███   ███    ███   ███    ███           ▄█    ███                    
 ▄████████▀    ███    █▀    █▀    ▄████▀       ▄████████▀                                                                                  
==========================================================================
        1. Start Game
        2. How to Play
        3. Quit
        """)
        
        choice = input("Enter your choice (1 or 2):\n")
        
        if choice == "1":
            get_username() # get the users username
            get_board_size() # Call function to get board size
            main_game(player_ship_lives, player_board, player_radar, 
                      ai_ship_lives, ai_board, ai_radar, 
                      ship_length, ship_position, orientation, 
                      total_hits, miss, turns_taken) # Call function to start the main game
        elif choice == "2":
            game_instructions() # Show game instructions
        elif choice == "3":
            print("Thank you for playing!") # Exit message
            exit()
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.") # Error message for invalid input

# Function to show game instructions
def game_instructions():
    print("""
    Welcome to Battleships!

    Objective:
    Sink all of your opponent's battleships before they sink yours!

    Game Overview:
    - You and the computer will each have a grid filled with ships.
    - Ships are placed in a line (either horizontally or vertically) and can be anywhere from 2 to 5 spaces in size.
    - Your goal is to guess where the enemy ships are located by choosing a row and column, trying to hit them!
    - The computer will also try to sink your ships, and it can detect if your ships are placed horizontally or vertically.
    
    How to Play:
    1. First, you will choose your grid size.
    2. Then, ships will be placed randomly on the grid (you cannot see where they are!).
    3. During each turn, you will pick a row and column to guess where an enemy ship might be.
    4. The computer will also try to guess your ship locations each turn.
    
    Your turn:
    - You will be asked to choose a column and a row (e.g., 1,1, 2,2) to fire at.
    - If you hit a ship, the computer will inform you that you’ve struck a ship.
    - If you miss, it will say that your guess was a miss.
    - There are a total of 17 ship parts for both you and the AI
    - You and the AI each have 5 Ships, one is 5 parts long, another is 4 parts long, 2 of them are 3 parts long and the last is 2 parts long

    The Computer's Turn:
    - The computer will also fire at a random location on your grid.
    - The computer uses its strategy to determine if your ships are positioned horizontally or vertically, so be careful!

    Ship Sizes:
    - Ships range from 2 to 5 spaces in length.
    
    End Game:
    - The game ends when either player sinks all of the opponent’s ships or all their ships are sunk.

    Ready to play? Let's get started!
    """)
    while True:
        try:
            back = int(input("Type 1 to go back:\n")) # Prompt user to return to main menu
            if back == 1:
                main_menu() # Go back to the main menu
                break
        except:
            print("Please enter a valid option!") # Error message for invalid input
            continue

# Function to initialize the game
def game_init():
    global player_radar
    global player_board
    global ai_radar
    global ai_board
    player_radar = [['O'] * cols for _ in range(rows)] # Create a radar board for the player
    player_board = [['O'] * cols for _ in range(rows)] # Create a board for the player
    ai_radar = [['O'] * cols for _ in range(rows)] # Create a radar board for the AI
    ai_board = [['O'] * cols for _ in range(rows)] # Create a board for the AI

    # Place ships for both player and AI
    for x in range(len(SHIPS)):
        player_board = place_ships(SHIPS[x], player_board, x) # Place player ships
        ai_board = place_ships(SHIPS[x], ai_board) # Place AI ships

# Function to prompt the user to choose the board size and difficulty
def get_board_size():
    global rows
    global cols
    while True:
        try:
            numOfGrid = int(input("""
Please pick the size of your grid and difficulty
1. 6x6 (Very Easy)
2. 7x7 (Easy)
3. 8x8 (Medium)
4. 9x9 (Hard)
5. 10x10 (Very Hard)
\n"""))
            if numOfGrid == 1:
                rows = 6 
                cols = 6
                game_init() # Initialize the game
                return rows, cols
            elif numOfGrid == 2:
                rows = 7
                cols = 7
                game_init() # Initialize the game
                return rows, cols
            elif numOfGrid == 3:
                rows = 8
                cols = 8
                game_init() # Initialize the game
                return rows, cols
            elif numOfGrid == 4:
                rows = 9
                cols = 9
                game_init() # Initialize the game
                return rows, cols
            elif numOfGrid == 5:
                rows = 10
                cols = 10
                game_init() # Initialize the game
                return rows, cols
            else:
                print("Invalid Response Please enter a number above")
                ValueError
        except ValueError:
            print("Error: Please enter valid integers.") # Error message for invalid input

# Initialize the sea with ocean spaces
for x in range(rows):
    SEA.append([OCEAN] * rows)

# Function to print the board for the player
def print_board():
    print("\n-------------------------------------------------------\n")
    # Print column headers based on the actual number of columns
    print("  " + " ".join(map(str, range(cols))) + " || " + " ".join(map(str, range(cols))))
    
    for i in range(rows):  # Iterate over the rows, not columns
        print(i, " ".join(player_radar[i]), "||", " ".join(player_board[i])) # Print each row of the player's radar and board

# Generate a random row to place a ship
def random_row(is_vertical, size):
    if is_vertical:
        return randint(0, rows - size) # If vertical, choose a row that fits the ship
    else:
        return randint(0, rows - 1) # If horizontal, choose any row

# Generate a random column to place a ship
def random_col(is_vertical, size):
    if is_vertical:
        return randint(0, cols - 1) # If vertical, choose any column
    else:
        return randint(size - 1, cols - 1) # If horizontal, choose a column that fits the ship

# Check if a given row and column is an ocean space
def is_ocean(row, col, b): # true if ocean
    if row < 0 or row >= rows: # If row is out of bounds
        return 0
    elif col < 0 or col >= cols: # If column is out of bounds
        return 0
    if b[row][col] == OCEAN: # Check if the space is ocean
        return 1
    else:
        return 0

# Additional function checking if the given coordinates are ocean
def is_oceanin(row, col, b):
    if type(row) is not int or type(col) is not int: # If row or column are not integers
        return 0
    if row < 0 or row >= rows: # If row is out of bounds
        return 0
    elif col < 0 or col >= cols: # If column is out of bounds
        return 0
    if b[row][col] == OCEAN: # Check if the space is ocean
        return 1
    else:
        return 0

# Define a function to place the ships on the board
def place_ships(size, board, set_ship = None):
    is_vertical = randint(0, 1)  # Randomly decide the orientation of the ship (vertical or horizontal)
    occupied = True  # Initially assume the ship will be placed in an occupied position
    while(occupied):  # Keep trying to place the ship until we find an empty spot
        occupied = False  # Reset occupied flag to check placement
        ship_row = random_row(is_vertical, size)  # Get a random starting row for the ship
        ship_col = random_col(is_vertical, size)  # Get a random starting column for the ship
        if is_vertical:  # If the ship is placed vertically, check each position it would occupy
            for p in range(size):
                if not is_ocean(ship_row + p, ship_col, board):  # Check if the space is free
                    occupied = True  # Mark as occupied if any part of the ship would overlap another ship
        else:  # If the ship is placed horizontally, check each position it would occupy
            for p in range(size):
                if not is_ocean(ship_row, ship_col - p, board):  # Check if the space is free
                    occupied = True  # Mark as occupied if any part of the ship would overlap another ship
    # Now place the ship on the board
    if is_vertical:
        board[ship_row][ship_col] = "^"  # Place the top of the ship
        board[ship_row + size - 1][ship_col] = "v"  # Place the bottom of the ship
        if set_ship != None:  # If a ship number is provided, mark the number on the ship's positions
            number_board[ship_row][ship_col] = set_ship
            number_board[ship_row + size - 1][ship_col] = set_ship
        for p in range(size - 2):  # Place the middle parts of the ship
            board[ship_row + p + 1][ship_col] = "+"
            if set_ship != None:
                number_board[ship_row + p + 1][ship_col] = set_ship
    else:  # Horizontal placement of the ship
        board[ship_row][ship_col] = ">"  # Place the right end of the ship
        board[ship_row][ship_col - size + 1] = "<"  # Place the left end of the ship
        if set_ship != None:  # If a ship number is provided, mark the number on the ship's positions
            number_board[ship_row][ship_col] = set_ship
            number_board[ship_row][ship_col - size + 1] = set_ship
        for p in range(size - 2):  # Place the middle parts of the ship
            board[ship_row][ship_col - p - 1] = "+"
            if set_ship != None:
                number_board[ship_row][ship_col - p - 1] = set_ship
    return board  # Return the updated board with the ship placed

# Function to get the ship number (size) at a specific position
def ship_number(r,c):
    if is_ocean(r,c, number_board):  # If the position is an ocean space, return -1
        return -1
    return SHIPS[number_board[r][c]]  # Otherwise, return the size of the ship at the position

# Check if a ship is sunk based on total hits
def ship_sunk():
    if total_hits.count(total_hits[0]) == ship_length[0]:  # If all parts of the ship are hit
        return 1  # The ship is sunk
    return 0  # The ship is not sunk yet

# Init the Boards (deep copy of SEA grid)
player_radar = copy.deepcopy(SEA)  # Radar for player (to track guesses)
player_board = copy.deepcopy(SEA)  # Player's actual ship placement
ai_radar = copy.deepcopy(SEA)  # Radar for AI (to track AI's guesses)
ai_board = copy.deepcopy(SEA)  # AI's actual ship placement
number_board = copy.deepcopy(SEA)  # Board to track ship numbers for validation

# Place the Ships on the player and the AI's Board
# Use the place_ships function to randomly place ships on both player and AI boards

# Define the main game loop
def main_game(player_ship_lives, player_board, player_radar, ai_ship_lives, ai_board, ai_radar, ship_length, ship_position, orientation, total_hits, miss, turns_taken):
    turns_taken = 0
    print_board()  # Print the current board
    while player_ship_lives and ai_ship_lives:  # Continue the game as long as both players have ships
        print("\n-------------------------------------------------------\n")
        try:
            col_guess = input("Guess Col (or type 'q' to quit):\n")  # Ask player for a column guess
            if col_guess.lower() == 'q':  # Check if player chose to quit
                print("You chose to quit. Goodbye!")
                break
            col_guess = int(col_guess)  # Convert column guess to an integer

            row_guess = input("Guess Row (or type 'q' to quit):\n")  # Ask player for a row guess
            if row_guess.lower() == 'q':  # Check if player chose to quit
                print("You chose to quit. Goodbye!")
                break
            row_guess = int(row_guess)  # Convert row guess to an integer
            turns_taken = turns_taken + 1
        except ValueError:  # Handle invalid input (non-integer values)
            print("Invalid input. Please enter valid row and column numbers.")
            continue
        
        # Ensure the guessed position is a valid ocean space
        while not is_oceanin(row_guess, col_guess, player_radar):
            print("Sorry that is an invalid shot")
            try:
                col_guess = int(input("Guess Col:\n"))  # Re-prompt the player for valid input
                row_guess = int(input("Guess Row:\n"))  # Re-prompt the player for valid input
            except:
                print("That is invalid, please enter an number")
                continue
        
        # Check if the player's guess hits a ship on the AI's board
        if ai_board[row_guess][col_guess] != OCEAN:
            ai_ship_lives -= 1  # Decrease the AI's remaining ship lives
            if ai_ship_lives:  # If the AI still has ships left, print a hit message
                print("You Hit an Enemy Ship!")
                player_radar[row_guess][col_guess] = HIT  # Mark the hit on the player's radar
            else:  # If the AI's ships are all sunk
                player_radar[row_guess][col_guess] = HIT  # Mark the hit on the player's radar
                print("Congratulations! You sunk my Battleship")  # Congratulate the player
                entry = [username, turns_taken]
                leaderboard = SHEET.worksheet("leaderboard")
                leaderboard.append_row(entry)
                break  # End the game if AI's ships are sunk
        else:  # If the guess was a miss
            print("\nYou Missed!")
            player_radar[row_guess][col_guess] = FIRE  # Mark the miss on the player's radar
        
        # AI's turn to guess
        print("\nTarget Orientation", orientation)  # Show the orientation of the AI's next shot
        if not len(ship_length):  # If the AI hasn't hit any ships yet, choose a random guess
            ai_row_guess = randint(0, rows-1)  # Generate random row for the AI's shot
            ai_col_guess = randint(0, cols-1)  # Generate random column for the AI's shot
            # Ensure the AI guesses an non ocean space
            while not is_ocean(ai_row_guess, ai_col_guess, ai_radar):
                ai_row_guess = randint(0, rows-1)
                ai_col_guess = randint(0, cols-1)
            if not is_ocean(ai_row_guess, ai_col_guess, player_board):  # Check if the AI hits a ship
                while ai_radar[ai_row_guess][ai_col_guess] == HIT:
                    ai_row_guess = randint(0, rows-1)  # Generate random row for the AI's shot
                    ai_col_guess = randint(0, cols-1)  # Generate random column for the AI's shot
                    break
                miss = 0  # Indicate that the shot was not a miss
                player_ship_lives -= 1  # Decrease player's remaining ship lives
                ship_length.append((ship_number(ai_row_guess, ai_col_guess)))  # Add ship part to the list
                ship_position.extend([ai_row_guess, ai_col_guess])  # Add the position to the list
                orientation = -1  # Reset the ship's orientation
                player_board[ai_row_guess][ai_col_guess] = HIT  # Mark the hit on the player's board
                ai_radar[ai_row_guess][ai_col_guess] = HIT  # Mark the hit on the AI's radar
                total_hits.append(number_board[ai_row_guess][ai_col_guess])  # Track the hit
                print("Attention Captain! You've been Hit!")
            else:  # If the AI misses, mark the miss on the board
                miss = 1
                player_board[ai_row_guess][ai_col_guess] = FIRE
                ai_radar[ai_row_guess][ai_col_guess] = FIRE
                print("\nThe Enemy Missed!!")
        else:  
            if orientation == -1:  
                print("Ship has no orientation")
                
                if len(ship_position) > 2:  # Ensure that there are at least 3 elements in ship_position
                    ai_col_guess = ship_position[1 + 1]  # Access the third element if available
                else:
                    # If ship_position doesn't have enough elements, handle the situation
                    ai_row_guess = ship_position[0]  # Default to the first element in ship_position
                    ai_col_guess = ship_position[1] if len(ship_position) > 1 else 0  # Default to 0 if there's only one element

                if is_ocean(ship_position[0] + 1, ship_position[1], ai_radar):
                    ai_row_guess = ship_position[0] + 1
                    ai_col_guess = ship_position[1]
                elif is_ocean(ship_position[0] - 1, ship_position[1], ai_radar):
                    ai_row_guess = ship_position[0] - 1
                    ai_col_guess = ship_position[1]
                elif is_ocean(ship_position[0], ship_position[1] - 1, ai_radar):
                    ai_row_guess = ship_position[0]
                    ai_col_guess = ship_position[1] - 1
                else:
                    ai_row_guess = randint(0, rows - 1)
                    ai_col_guess = randint(0, cols - 1)
            elif orientation:  # If the AI has determined the ship's orientation is vertical, adjust accordingly
                for item in ai_radar:
                    print(item[0], ' '.join(map(str, item[1:])))
                if is_ocean(ai_row_guess + 1, ai_col_guess, ai_radar) and not miss:
                    ai_row_guess += 1
                else:
                    ai_row_guess -= 1
                    while not is_ocean(ai_row_guess, ai_col_guess, ai_radar):
                        ai_row_guess -= 1
            
            else:  # If the orientation is horizontal, adjust the AI's shot in that direction
                for item in ai_radar:
                    print(item[0], ' '.join(map(str, item[1:])))
                if is_ocean(ai_row_guess, ai_col_guess - 1, ai_radar) and not miss:
                    ai_col_guess = ai_col_guess - 1
                else:
                    ai_col_guess = ai_col_guess + 1
                    while not is_ocean(ai_row_guess, ai_col_guess, ai_radar):
                        ai_col_guess += 1

            if not is_ocean(ai_row_guess, ai_col_guess, player_board):  # If AI hits a ship
                player_board[ai_row_guess][ai_col_guess] = HIT  # Mark the hit on player's board
                ai_radar[ai_row_guess][ai_col_guess] = HIT  # Mark the hit on AI's radar
                total_hits.append(number_board[ai_row_guess][ai_col_guess])  # Track the hit
                player_ship_lives -= 1  # Decrease the player's remaining ship lives
                
                # Check if the AI has found the orientation of the ship
                if total_hits.count(total_hits[0]) == 2 and ship_number(ai_row_guess, ai_col_guess) == ship_number(ship_position[0], ship_position[1]):
                    if ai_col_guess != ship_position[1]:
                        orientation = 0
                    else:
                        orientation = 1
                    print("New Orientation: ", orientation)
                elif total_hits[0] != number_board[ai_row_guess][ai_col_guess]:
                    ship_length.append((ship_number(ai_row_guess, ai_col_guess)))  # Update the ship length
                    ship_position.extend([ai_row_guess, ai_col_guess])  # Add new ship position
                if player_ship_lives:  # If the player still has ships left, continue the game
                    miss = 0
                    print("Captain We've Been Hit!!")
                else:  # If the player is out of ships, declare AI as the winner
                    print("We're going down, Abandon Ship!!")
                    print_board()  # Print final game state
                    print("\n-------------------------------------------------------\n")
                    play_again = input("You Lose!! Would you like to play again y/n?:\n")
                    if play_again == "y":  # If player wants to play again, restart the game
                        main_game(player_ship_lives, player_board, player_radar, ai_ship_lives, ai_board, ai_radar, ship_length, ship_position, orientation, total_hits, miss, turns_taken)
                        break
                    else:
                        exit()  # Exit the game if the player chooses not to play again
                    break
            else:  # If AI misses, mark the miss on the board
                miss = 1
                player_board[ai_row_guess][ai_col_guess] = FIRE
                ai_radar[ai_row_guess][ai_col_guess] = FIRE
                print("\nThe Enemy Missed!!")
            if ship_sunk():  # Check if any ship has been sunk
                orientation = -1  # Reset ship orientation after sinking
                ship_position.pop(0)  # Remove first position from the ship's position list
                ship_position.pop(0)  # Remove second position from the ship's position list
                ship_length.pop(0)  # Remove the sunk ship's length from the list
                t = total_hits[0]  # Identify the ship that was sunk
                for x in range(total_hits.count(t)):  # Remove all parts of the sunk ship from the total hits
                    total_hits.remove(t)
                if len(ship_length) != 0:  # If the player still has ships left, reset miss flag
                    miss = 0
                else:  # If no ships left, set miss flag
                    miss = 1
        print_board()  # Print the updated game board

print("Lets Play Battleships!!")  # Welcome message
main_menu()  # Start the main menu to begin the game
