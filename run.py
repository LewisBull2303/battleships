from random import randint
import copy
import os
import time
import gspread
from tabulate import tabulate
from colors import Colors as Col
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
OCEAN = (Col.BLUE + 'O' + Col.RESET) # Icon for the ocean spaces
FIRE = (Col.WHITE + "X" + Col.RESET) # Icon for a miss
HIT = (Col.RED + "*" + Col.RESET) # Icon for a hit
SHIPS = [5, 4, 3, 3, 2] # Sizes of the ships
SEA = [] # Empty list for the sea (grid)

orientation = -1 # Stores the ship's hit orientation
total_hits = [] # Stores the ship number every time the bot hits a ship
miss = 1 # Stores whether the last AI shot was a miss
turns_taken = 0 #Stores the number of turns taken for the leaderboard
username = "PLACEHOLDER"

player_ship_lives = 1 # The amount of lives for the player (equal to the ships)
ship_position = [] 
ship_length = []

player_radar = [] # The radar board for the player
player_board = [] # The board representing player ships' positions
ai_radar = [] # The radar board for the AI
ai_board = [] # The board representing AI ships' positions
ai_ship_lives = 17 # The AI lives (equal to the ship parts)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_username():
    global username
    username = input("\nPlease enter your username: \n")
    return username

def get_leaderboard_entries():
    leaderboard = SHEET.worksheet("sorted_leaderboard")
    score = leaderboard.get("A1:B11")
    print(tabulate(score))
    

# Main menu function for selecting options
def main_menu():
    while True:
        clear_screen()
        print("""
==========================================================================      
██████╗  █████╗ ████████╗████████╗██╗     ███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
██████╔╝███████║   ██║      ██║   ██║     █████╗  
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
                                                  
███████╗██╗  ██╗██╗██████╗ ███████╗               
██╔════╝██║  ██║██║██╔══██╗██╔════╝               
███████╗███████║██║██████╔╝███████╗               
╚════██║██╔══██║██║██╔═══╝ ╚════██║               
███████║██║  ██║██║██║     ███████║               
╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝               
==========================================================================
        1. Start Game
        2. How to Play
        3. Leaderboard
        4. Quit
        """)
        
        choice = input("Enter your choice (1, 2, 3 or 4):\n")
        
        if choice == "1":
            clear_screen()
            get_username() # get the users username
            get_board_size() # Call function to get board size
            clear_screen()
            print("Loading...")
            time.sleep(1)
            main_game(player_ship_lives, player_board, player_radar, 
                      ai_ship_lives, ai_board, ai_radar, 
                      ship_length, ship_position, orientation, 
                      total_hits, miss, turns_taken) # Call function to start the main game
        elif choice == "2":
            print("\nLoading...")
            time.sleep(1)
            game_instructions() # Show game instructions
        elif choice == "3":
            print("\nLoading...")
            time.sleep(1)
            clear_screen()
            get_leaderboard_entries() #Shows the Leaderboard of the top 10 players
            back = input("Press any key to return to the main menu:\n")
        elif choice == "4":
            print("Thank you for playing!") # Exit message
            exit()
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.") # Error message for invalid input

# Function to show game instructions
def game_instructions():
    clear_screen()
    print("""
Welcome to Battleships!
    
Objective: Sink all enemy ships before yours are sunk!

How to Play:

You and the AI each have a grid with 5 hidden ships (sizes: 5, 4, 3, 3, 2).
Take turns guessing coordinates to hit enemy ships.
The AI will also fire at your grid strategically.
First to sink all 17 enemy ship parts wins!
Ready? Let’s play!
    """)
    back = input("Type any key to return to the main menu: \n")
    main_menu()

# Function to initialize the game
def game_init():
    
    global player_radar
    global player_board
    global ai_radar
    global ai_board
    player_radar = [[Col.BLUE + 'O' + Col.RESET] * cols for _ in range(rows)] # Create a radar board for the player
    player_board = [[Col.BLUE + 'O' + Col.RESET] * cols for _ in range(rows)] # Create a board for the player
    ai_radar = [[Col.BLUE + 'O' + Col.RESET] * cols for _ in range(rows)] # Create a radar board for the AI
    ai_board = [[Col.BLUE + 'O' + Col.RESET] * cols for _ in range(rows)] # Create a board for the AI

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
    if cols == 6:
        print("  CPUs Board" + "     " + f"{username}'s Board")
    elif cols == 7:
        print("  CPUs Board" + "       " + f"{username}'s Board")
    elif cols == 8:
        print("  CPUs Board" + "         " + f"{username}'s Board")
    elif cols == 9:
        print("  CPUs Board" + "           " + f"{username}'s Board")
    else:
        print("  CPUs Board" + "             " + f"{username}'s Board")
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
    if b[row][col] == (Col.BLUE + "O" + Col.RESET): # Check if the space is ocean
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
        board[ship_row][ship_col] = (Col.GREY + "^" + Col.RESET)  # Place the top of the ship
        board[ship_row + size - 1][ship_col] = (Col.GREY + "v" + Col.RESET)  # Place the bottom of the ship
        if set_ship != None:  # If a ship number is provided, mark the number on the ship's positions
            number_board[ship_row][ship_col] = set_ship
            number_board[ship_row + size - 1][ship_col] = set_ship
        for p in range(size - 2):  # Place the middle parts of the ship
            board[ship_row + p + 1][ship_col] = (Col.GREY + "+" + Col.RESET)
            if set_ship != None:
                number_board[ship_row + p + 1][ship_col] = set_ship
    else:  # Horizontal placement of the ship
        board[ship_row][ship_col] = (Col.GREY + ">" + Col.RESET)  # Place the right end of the ship
        board[ship_row][ship_col - size + 1] = (Col.GREY + "<" + Col.RESET)  # Place the left end of the ship
        if set_ship != None:  # If a ship number is provided, mark the number on the ship's positions
            number_board[ship_row][ship_col] = set_ship
            number_board[ship_row][ship_col - size + 1] = set_ship
        for p in range(size - 2):  # Place the middle parts of the ship
            board[ship_row][ship_col - p - 1] = (Col.GREY + "+" + Col.RESET)
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
                clear_screen()
                break
            col_guess = int(col_guess)  # Convert column guess to an integer

            row_guess = input("Guess Row (or type 'q' to quit):\n")  # Ask player for a row guess
            if row_guess.lower() == 'q':  # Check if player chose to quit
                print("You chose to quit. Goodbye!")
                clear_screen()
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
                print("\nYou Hit an Enemy Ship!\n")
                print(f"Our Scanners indicate that the enemy still has {ai_ship_lives} ship parts left!")
                player_radar[row_guess][col_guess] = HIT  # Mark the hit on the player's radar
            else:  # If the AI's ships are all sunk
                player_radar[row_guess][col_guess] = HIT  # Mark the hit on the player's radar

                print("Congratulations! You win! You sunk all my Battleships")  # Congratulate the player
                leaderboard_entry = input(f"You won! Would you like to upload your score to the leaderboard? (y/n) \nYour Score: {turns_taken}\n")
                while True:
                    if leaderboard_entry.lower() == "y":
                        print("Uploading...")
                        time.sleep(1)
                        entry = [username, turns_taken]
                        leaderboard = SHEET.worksheet("leaderboard")
                        leaderboard.append_row(entry)
                        print("Uploaded!")
                        break
                    elif leaderboard_entry.lower() == "n":
                        print("Score Deleted")
                        break
                    else:
                        print("Please enter a valid option")
                        continue

                while True:
                    play_again = input("Would you like to play again? (y/n)\n")
                    if play_again.lower == "y":
                        print("Loading...")
                        time.sleep(1)
                        main_menu()
                        break
                    elif play_again.lower() == "n":
                        print("Thanks for playing!")
                        exit
                        break
                    else:
                        print("Please enter a valid option")
                        continue
                break  # End the game if AI's ships are sunk
        else:  # If the guess was a miss
            print("\nYou Missed!")
            player_radar[row_guess][col_guess] = FIRE  # Mark the miss on the player's radar
        
        # AI's turn to guess
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
                print("\nAttention Captain! You've been Hit!")
            else:  # If the AI misses, mark the miss on the board
                miss = 1
                player_board[ai_row_guess][ai_col_guess] = FIRE
                ai_radar[ai_row_guess][ai_col_guess] = FIRE
                print("\nThe Enemy Missed!!")
        else:  
            if orientation == -1:  
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
                if is_ocean(ai_row_guess + 1, ai_col_guess, ai_radar) and not miss:
                    ai_row_guess += 1
                else:
                    ai_row_guess -= 1
                    while not is_ocean(ai_row_guess, ai_col_guess, ai_radar):
                        ai_row_guess -= 1
            
            else:  # If the orientation is horizontal, adjust the AI's shot in that direction
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
                elif total_hits[0] != number_board[ai_row_guess][ai_col_guess]:
                    ship_length.append((ship_number(ai_row_guess, ai_col_guess)))  # Update the ship length
                    ship_position.extend([ai_row_guess, ai_col_guess])  # Add new ship position
                if player_ship_lives:  # If the player still has ships left, continue the game
                    miss = 0
                    print("\nCaptain We've Been Hit!!")
                else:  # If the player is out of ships, declare AI as the winner
                    print("\nOh no! All of your battleships have been sunk!")
                    print("\n-------------------------------------------------------\n")
                    play_again = input("You Lose!! Would you like to play again y/n?:\n")
                    if play_again == "y":  # If player wants to play again, restart the game
                        main_menu()
                        break
                    else:
                        print("\n Thanks for playing!")
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

main_menu()  # Start the main menu to begin the game
