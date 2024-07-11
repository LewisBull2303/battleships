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

def print_board():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(" 0 1 2 3 4 5 6 7 8 9 || 0 1 2 3 4 5 6 7 8 9")
    i = 0
    for row in range(SIZE):
        print(i, " ".join(player_radar[row]), "||", " ".join(player_board[row]))

def random_row(is_vertical, size):
    if is_vertical:
        return randint(0, SIZE - size)
    else:
        return randint(0, SIZE - 1)

def random_col(is_vertical, size):
    if is_vertical:
        return randint(0, SIZE - size)
    else:
        return randint(0, SIZE - 1)
    
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
