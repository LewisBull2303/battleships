from random import randint
import copy

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

player_ship_lives = 17 # The amount of lives for the player (equal to the ships)
ship_position = [] 
ship_length = []

player_radar = [] # The radar board for the player
player_board = [] # The board representing player ships' positions
ai_radar = [] # The radar board for the AI
ai_board = [] # The board representing AI ships' positions
ai_ship_lives = 17 # The AI lives (equal to the ship parts)

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
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            get_board_size() # Call function to get board size
            main_game(player_ship_lives, player_board, player_radar, 
                      ai_ship_lives, ai_board, ai_radar, 
                      ship_length, ship_position, orientation, 
                      total_hits, miss) # Call function to start the main game
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
            back = int(input("Type 1 to go back: ")) # Prompt user to return to main menu
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
1. 5x5 (Very Easy)
2. 6x6 (Easy)
3. 7x7 (Medium)
4. 8x8 (Hard)
5. 9x9 (Very Hard)
6. 10x10 (Super Hard!)
"""))
            if numOfGrid == 1:
                rows = 5
                cols = 5
                game_init() # Initialize the game
                return rows, cols
            elif numOfGrid == 2:
                rows = 6
                cols = 6
                print(rows, cols)
                game_init() # Initialize the game
                return rows, cols
            elif numOfGrid == 3:
                rows = 7
                cols = 7
                print(rows, cols)
                game_init() # Initialize the game
                return rows, cols
            elif numOfGrid == 4:
                rows = 8
                cols = 8
                game_init() # Initialize the game
                return rows, cols
            elif numOfGrid == 5:
                rows = 9
                cols = 9
                game_init() # Initialize the game
                return rows, cols
            elif numOfGrid == 6:
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
    is_vertical = randint(0, 1)
    occupied = True
    while(occupied):
        occupied = False
        ship_row = random_row(is_vertical, size)
        ship_col = random_col(is_vertical, size)
        if is_vertical:
            for p in range(size):
                if not is_ocean(ship_row + p, ship_col, board):
                    occupied = True
        else:
            for p in range(size):
                if not is_ocean(ship_row, ship_col - p, board):
                    occupied = True
    if is_vertical:
        board[ship_row][ship_col] = "^"
        board[ship_row + size - 1][ship_col] = "v"
        if set_ship != None:
            number_board[ship_row][ship_col] = set_ship
            number_board[ship_row + size - 1][ship_col] = set_ship
        for p in range(size -2):
            board[ship_row + p + 1][ship_col] = "+"
            if set_ship != None:
                number_board[ship_row + p + 1][ship_col] = set_ship
    else:
        board[ship_row][ship_col] = ">"
        board[ship_row][ship_col - size + 1] = "<"
        if set_ship != None:
            number_board[ship_row][ship_col] = set_ship
            number_board[ship_row][ship_col - size + 1] = set_ship
        for p in range(size - 2):
            board[ship_row][ship_col - p - 1] = "+"
            if set_ship != None:
                number_board[ship_row][ship_col - p - 1] = set_ship
    return board

def ship_number(r,c):
    if is_ocean(r,c, number_board):
        return -1
    return SHIPS[number_board[r][c]]

def ship_sunk():
    if total_hits.count(total_hits[0]) == ship_length[0]:
        return 1
    return 0    

# Init the Boards
player_radar = copy.deepcopy(SEA)
player_board = copy.deepcopy(SEA)
ai_radar = copy.deepcopy(SEA)
ai_board = copy.deepcopy(SEA)
number_board = copy.deepcopy(SEA)

# Place the Ships on the player and the AI's Board

# Define the main game loop
def main_game(player_ship_lives, player_board, player_radar, ai_ship_lives, ai_board, ai_radar, ship_length, ship_position, orientation, total_hits, miss):
    print_board()
    while player_ship_lives and ai_ship_lives:
        print("\n-------------------------------------------------------\n")
        try:
            row_guess = input("Guess Row (or type 'q' to quit): ")
            if row_guess.lower() == 'q':
                print("You chose to quit. Goodbye!")
                break
            row_guess = int(row_guess)
            
            col_guess = input("Guess Col (or type 'q' to quit): ")
            if col_guess.lower() == 'q':
                print("You chose to quit. Goodbye!")
                break
            col_guess = int(col_guess)
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")
            continue
        
        while not is_oceanin(row_guess, col_guess, player_radar):
            print("Sorry that is an invalid shot")
            row_guess = int(input("Guess Row: "))
            col_guess = int(input("Guess Col: "))
        
        if ai_board[row_guess][col_guess] != OCEAN:
            ai_ship_lives -= 1
            if ai_ship_lives:
                print("You Hit an Enemy Ship!")
                player_radar[row_guess][col_guess] = HIT
            else:
                player_radar[row_guess][col_guess] = HIT
                print("Congratulations! You sunk my Battleship")
                break
        else:
            print("\nYou Missed!")
            player_radar[row_guess][col_guess] = FIRE
        
        print("Target Orientation", orientation)
        if not len(ship_length):
            second_shot = 0
            ai_row_guess = randint(0, rows-1)
            ai_col_guess = randint(0, cols-1)
            while not is_ocean(ai_row_guess, ai_col_guess, ai_radar):
                ai_row_guess = randint(0, rows-1)
                ai_col_guess = randint(0, cols-1)
            if not is_ocean(ai_row_guess, ai_col_guess, player_board):
                miss = 0
                player_ship_lives -= 1
                ship_length.append((ship_number(ai_row_guess, ai_col_guess)))
                ship_position.extend([ai_row_guess, ai_col_guess])
                orientation = -1
                player_board[ai_row_guess][ai_col_guess] = HIT
                ai_radar[ai_row_guess][ai_col_guess] = HIT
                total_hits.append(number_board[ai_row_guess][ai_col_guess])
                print("Attention Captain! You've been Hit!")
            else:
                miss = 1
                player_board[ai_row_guess][ai_col_guess] = FIRE
                ai_radar[ai_row_guess][ai_col_guess] = FIRE
                print("\nThe Enemy Missed!!")
        else:
            if orientation == -1:
                print("Ship has no orientation")
                if is_ocean(ship_position[0]+1, ship_position[1], ai_radar):
                    ai_row_guess = ship_position[0] + 1
                    ai_col_guess = ship_position[1]
                elif is_ocean(ship_position[0] - 1, ship_position[1], ai_radar):
                    ai_row_guess = ship_position[0] - 1
                    ai_col_guess = ship_position[1]
                elif is_ocean(ship_position[0], ship_position[1] - 1, ai_radar):
                    ai_row_guess = ship_position[0]
                    ai_col_guess = ship_position[1] - 1
                else:
                    ai_row_guess = ship_position[0]
                    ai_col_guess = ship_position[1 + 1]
            elif orientation:
                for item in ai_radar:
                    print(item[0], ' '.join(map(str, item[1:])))
                if is_ocean(ai_row_guess + 1, ai_col_guess, ai_radar) and not miss:
                    ai_row_guess += 1
                else:
                    ai_row_guess -= 1
                    while not is_ocean(ai_row_guess, ai_col_guess, ai_radar):
                        ai_row_guess -= 1
            
            else:
                for item in ai_radar:
                    print(item[0], ' '.join(map(str, item[1:])))
                if is_ocean(ai_row_guess, ai_col_guess - 1, ai_radar) and not miss:
                    ai_col_guess = ai_col_guess - 1
                else:
                    ai_col_guess = ai_col_guess + 1
                    while not is_ocean(ai_row_guess, ai_col_guess, ai_radar):
                        ai_col_guess += 1

            if not is_ocean(ai_row_guess, ai_col_guess, player_board):
                player_board[ai_row_guess][ai_col_guess] = HIT
                ai_radar[ai_row_guess][ai_col_guess] = HIT
                total_hits.append(number_board[ai_row_guess][ai_col_guess])
                player_ship_lives -= 1
                
                if total_hits.count(total_hits[0]) == 2 and ship_number(ai_row_guess, ai_col_guess) == ship_number(ship_position[0], ship_position[1]):
                    if ai_col_guess != ship_position[1]:
                        orientation = 0
                    else:
                        orientation = 1
                    print("New Orientation: ", orientation)
                elif total_hits[0] != number_board[ai_row_guess][ai_col_guess]:
                    ship_length.append((ship_number(ai_row_guess, ai_col_guess)))
                    ship_position.extend([ai_row_guess, ai_col_guess])
                if player_ship_lives:
                    miss = 0
                    print("Captain We've Been Hit!!")
                else:
                    print("We're going down, Abandon Ship!!")
                    print_board()
                    print("\n-------------------------------------------------------\n")
                    play_again = input("You Lose!! Would you like to play again y/n?: ")
                    if play_again == "y":
                        main_game(player_ship_lives, player_board, player_radar, ai_ship_lives, ai_board, ai_radar, ship_length, ship_position, orientation, total_hits, miss)
                        break
                    else:
                        exit()
                    break
            else:
                miss = 1
                player_board[ai_row_guess][ai_col_guess] = FIRE
                ai_radar[ai_row_guess][ai_col_guess] = FIRE
                print("\nThe Enemy Missed!!")
            if ship_sunk():
                orientation = -1
                ship_position.pop(0)
                ship_position.pop(0)
                ship_length.pop(0)
                t = total_hits[0]
                for x in range(total_hits.count(t)):
                    total_hits.remove(t)
                if len(ship_length) != 0:
                    miss = 0
                else:
                    miss = 1
        print_board()

print("Lets Play Battleships!!")
main_menu()
