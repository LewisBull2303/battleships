from random import randint
import copy

OCEAN = "O"
FIRE = "X"
HIT = "*"
SIZE = 10
SHIPS = [5, 4, 3, 3, 2]
SEA = []

orientation = -1
total_hits = []
miss = 1

player_ship_lives = 17
player_radar = []
player_board = []

ai_ship_lives = 17
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
        
