from random import randint
import copy

rows = 10
cols = 10

#Setting up the Constants and variables
OCEAN = "O" #icon for the ocean spaces
FIRE = "X" # icon for a miss
HIT = "*" #icon for a hit
SHIPS = [5, 4, 3, 3, 2] # size of each of the ships
SEA = [] #empty list for the sea

orientation = -1 # stores the ships hit orientation.
total_hits = [] #stores the ship number everytime the bot hits a ship
miss = 1 #stores whether the last ai shot was a miss

player_ship_lives = 17 #the amount of lives for the player equal to the ships
ship_position = [] 
ship_length = []

player_radar = []
player_board = []
ai_ship_lives = 17 #the Ai lives equal to the ship parts
ai_radar = []
ai_board = []
ai_ship_lives = 17 #the Ai lives equal to the ship parts

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
        2. Quit
        """)
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            get_board_size()
            main_game(player_ship_lives, player_board, player_radar, 
                      ai_ship_lives, ai_board, ai_radar, 
                      ship_length, ship_position, orientation, 
                      total_hits, miss)
        elif choice == "2":
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def game_init():
    global player_radar
    global player_board
    global ai_radar
    global ai_board
    player_radar = [['O'] * cols for _ in range(rows)]
    player_board = [['O'] * cols for _ in range(rows)]
    ai_radar = [['O'] * cols for _ in range(rows)]
    ai_board = [['O'] * cols for _ in range(rows)]

    for x in range(len(SHIPS)):
        player_board = place_ships(SHIPS[x], player_board, x)
        ai_board = place_ships(SHIPS[x], ai_board)

# Prompt the user for the number of rows and columns
def get_board_size():
    global rows
    global cols
    global player_radar
    global player_board
    global ai_radar
    global ai_board
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
                game_init()
                return rows, cols
            elif numOfGrid == 2:
                rows = 6
                cols = 6
                print(rows, cols)
                game_init()
                return rows, cols
            elif numOfGrid == 3:
                rows = 7
                cols = 7
                print(rows, cols)
                game_init()
                return rows, cols
            elif numOfGrid == 4:
                rows = 8
                cols = 8
                game_init()
                return rows, cols
            elif numOfGrid == 5:
                rows = 9
                cols = 9
                game_init()
                return rows, cols
            elif numOfGrid == 6:
                rows = 10
                cols = 10
                game_init()
                return rows, cols
            else:
                print("Invalid Response Please enter a number above")
                ValueError
        except ValueError:
            print("Error: Please enter valid integers.")
for x in range(rows):
    SEA.append([OCEAN] * rows)

# Define a function to print the board the player will use
def print_board():
    print("\n-------------------------------------------------------\n")
    # Print column headers based on the actual number of columns
    print("  " + " ".join(map(str, range(cols))) + " || " + " ".join(map(str, range(cols))))
    
    for i in range(rows):  # Iterate over the rows, not columns
        print(i, " ".join(player_radar[i]), "||", " ".join(player_board[i]))

# Generate a Random row to place the ship
def random_row(is_vertical, size):
    if is_vertical:
        return randint(0, rows - size)
    else:
        return randint(0, rows - 1)

# Generate a Random Column to place the ship
def random_col(is_vertical, size):
    if is_vertical:
        return randint(0, cols - 1)
    else:
        return randint(size - 1, cols - 1)

# Check if the given row and col is an ocean space
def is_ocean(row, col, b): # true if ocean
    if row < 0 or row >= rows:
        return 0
    elif col < 0 or col >= cols:
        return 0
    if b[row][col] == OCEAN:
        return 1
    else:
        return 0

def is_oceanin(row,col,b):
    if type(row) is not int or type(col) is not int:
        return 0
    if row < 0 or row >= rows:
        return 0
    elif col < 0 or col >= cols:
        return 0
    if b[row][col] == OCEAN:
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
