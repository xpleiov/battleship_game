from random import randint


board = []
grid = int(input("To start the game enter the grid amount you want top play with and press ENTER: "))


def board_print(board):
    for x in range(grid):
        board.append(["0"] * grid)
    for row in board:
        print(" ".join(row))

board_print(board)
row, column = randint(0,len(board) - 1), randint(0,len(board) - 1)

# print(row, column) Used for testiing

while True:
    player_row, player_col= input("Guess Row:"), input("Guess Col:")

    if player_row == "Q" or player_col == "Q":
        print("You ended the game early")
        break

    player_row, player_col = int(player_row), int(player_col)

    elif player_row == row and player_col == column:
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
        print("You MISSED")
        board[player_row][player_col] = "-"
        print("-"*grid * 2)
        for row in board:
            print(" ".join(row))




