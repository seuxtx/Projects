#code terminal project
#Brandon Salter 7/1/23

from random import randint
#creates the game board in a 9x9 square
HIDDEN_BOARD = [[' '] * 9 for x in range(9)]
GUESS_BOARD = [[' '] * 9 for x in range(9)]

#converts the letters to numbers for the grid
letters_to_numbers = {'A' : 0,'B' : 1,'C' : 2,'D' : 3,'E' : 4,'F' : 5,'G' : 6,'H' : 7,'I' : 8}


#prints the board layout
def print_board(board):
   print('    A B C D E F G H I')
   print('    -----------------')
   row_number = 1
   for row in board:
       print("%d| %s|" % (row_number, "|".join(row)))
       row_number += 1

#creates the number of ships for the game
def create_ships(board):
    for ship in range(8):
        ship_row, ship_column = randint(0,8), randint(0,8)

        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,8), randint(0,8)
        board[ship_row][ship_column] = 'X'

#randomly decides where the ships will spawn in with every bootup
def get_ship_location():
    row = input('Please pick a location for a ship row 1-9')
    while row not in '1 2 3 4 5 6 7 8 9':
        print('Please place your ship inside row 1-9 ')
        row = input('Please pick a location for a ship row 1-9 ')
    column = input('Please place your ship in a ship column A-I ').upper()
    while column not in 'ABCDEFGHI':
        print('Please place your ship inside column A-I ')
        column = input('Please place your ship in a ship column A-I ').upper()
    return int(row) - 1,letters_to_numbers[column]
#checks if you hit the ship in the location you guessed
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

#hidden board is the board where the ships are stored and the guess board is the guess board where it will show the hits or misses depending on where the ships are located on hidden board
create_ships(HIDDEN_BOARD)
turns = 20
while turns > 0:
    print('Welcome to Battleship, the thinking game')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print('You Already fired on that location')
    elif HIDDEN_BOARD [row][column] == 'X':
        print('Enemy ship has been hit')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('You missed the enemy')
        GUESS_BOARD[row][column] = '-'
    if count_hit_ships(GUESS_BOARD) == 8:
        print('You won the game by sinking all your opponet battleships')
        break
    print( 'You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Game over, Ran out of turns')

#Test code to see how the boards displayed in the terminal
#shows if the game is running
#print_board(HIDDEN_BOARD)
#print_board(GUESS_BOARD)

