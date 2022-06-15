from random import randint


board = []
turns = []
grid = int(input("To start the game enter the grid amount you want top play with and press ENTER:\n"))
tries = int(input("Also please the number of tries you want to sinck my ship and press ENTER: \n"))



def board_print(board):
    for x in range(grid):
        board.append(["0"] * grid)
    for row in board:
        print(" ".join(row))

board_print(board)
row, column = randint(0,len(board) - 1), randint(0,len(board) - 1)

#print(row, column)# Used for testiing

while True:
    player_row, player_col= int(input("Guess Row:\n")), int(input("Guess Col:\n"))

    if player_row == row and player_col == column:
         board[player_row][player_col] = "X"
         print("-"*grid * 2)
         for row in board:
            print(" ".join(row))
         print("Hit!")
         break

    elif player_row > len(board) > player_col:
        print("invalid inputs")

    elif board[player_row][player_col] == "-":
        print("You have already guessed that")
        
    else:
        board[player_row][player_col] = "-"
        print("-"*grid * 2)
        for row in board:
            print(" ".join(row))
        print("You MISSED")
        turns.append([1])
        if tries == (len(turns) - 1):
            print("You have used all your {} tries".format(tries))
            print("Game over")
            break


