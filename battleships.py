from random import randint
import copy

#Setting up the Constants and variables
OCEAN = "O" #icon for the ocean spaces
FIRE = "X" # icon for a miss
HIT = "*" #icon for a hit
SIZE = 10 #size of the board
SHIPS = [5, 4, 3, 3, 2] # size of each of the ships
SEA = [] #empty list for the sea

orientation = -1 # stores the ships hit orientation.
total_hits = [] #stores the ship number everytime the bot hits a ship
miss = 1 #stores whether the last ai shot was a miss

player_ship_lives = 17 #the amount of lives for the player equal to the ships
player_radar = []
player_board = []

ai_ship_lives = 17 #the Ai lives equal to the ship parts
ai_radar = []
ai_board = []
ship_position = [] 
ship_length = []

for x in range(SIZE):
    SEA.append([OCEAN] * SIZE)

#Define a function to print the board the player will use
def print_board():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(" 0 1 2 3 4 5 6 7 8 9 || 0 1 2 3 4 5 6 7 8 9")
    i = 0
    for row in range(SIZE):
        print(i, " ".join(player_radar[row]), "||", " ".join(player_board[row]))

#Generate a Random row to place the ship
def random_row(is_vertical, size):
    if is_vertical:
        return randint(0, SIZE - size)
    else:
        return randint(0, SIZE - 1)

#Generate a Random Column to place the ship
def random_col(is_vertical, size):
    if is_vertical:
        return randint(0, SIZE - size)
    else:
        return randint(0, SIZE - 1)
    
#Check if the given row and col is an ocean space
def is_ocean(row, col, b):
    if row < 0 or row >= SIZE:
        return 0
    elif col < 0 or col >= SIZE:
        return 0
    if b[row][col] == OCEAN:
        return 1
    else:
        return 0

def is_oceanin(row, col, b):
    if type(row) is not int or type(col) is not int:
        return 0
    if row < 0 or row >= SIZE:
        return 0
    elif col < 0 or col >= SIZE:
        return 0
    if b[row][col] == OCEAN:
        return 1
    else:
        return 0

#Define a function to place the ships on the board
def place_ships(size, board, set_ship = None):
    is_vertical = randint(0, 1)
    occupied = True
    while(occupied):
        occupied = False
        ship_row = random_row(is_vertical, size)
        ship_col = random_col(is_vertical, size)
        if is_vertical:
            for p in range(size):
                if not is_ocean(ship_row+p, ship_col, board):
                    occupied = True
        else:
            for p in range(size):
                if not is_ocean(ship_row, ship_col-p, board):
                    occupied = True
        
        if is_vertical:
            board[ship_row][ship_col] = "^"
            board[ship_row + size-1][ship_col] = "v"
            if set_ship != None:
                number_board[ship_row][ship_col] = set_ship
                number_board[ship_row+ size - 1][ship_col] = set_ship
            for p in range(size - 2):
                board[ship_row + p + 1][ship_col] = "+"
                if set_ship != None:
                    number_board[ship_row + p + 1][ship_col] = set_ship
        else:
            board[ship_row][ship_col] = ">"
            board[ship_row][ship_col - size + 1] = set_ship
            if set_ship != None:
                number_board[ship_row][ship_col] = set_ship
                number_board[ship_row][ship_col - size + 1] = set_ship
            for p in range(size - 2):
                board[ship_row][ship_col-size+1] = "+"
                if set_ship != None:
                    number_board[ship_row][ship_col-p-1] = set_ship
        return board
    
def ship_number(r,c):
    if is_ocean(r,c, number_board):
        return -1
    return SHIPS[number_board[r][c]]

def ship_sunk():
    if total_hits.count(total_hits[0]) == ship_length[0]:
        return 1
    return 0    

#Init the Boards
player_radar = copy.deepcopy(SEA)
player_board = copy.deepcopy(SEA)
ai_radar = copy.deepcopy(SEA)
ai_board = copy.deepcopy(SEA)
number_board = copy.deepcopy(SEA)

#Place the Ships on the player and the AI's Board
for x in range(len(SHIPS)):
    player_board = place_ships(SHIPS[x], player_board, x)
    ai_board = place_ships(SHIPS[x], ai_board)

#Define the main game loop
print("Lets Play Battleships!!")
print_board()
