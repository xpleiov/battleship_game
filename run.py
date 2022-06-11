from random import randint

board = []

alpha = ["A","B","C","D","E",
         "F","G","H","I","J",
         "K","L","M","N","O",
         "P","Q","R","S","T",
         "U","V","W","X","Y","Z",
         ]

numbers = [1,2,3,4,5,6,7,8,9,10,11,
          12,13,14,15,16,17,18,19,
          20,21,22,23,24,25,26,
          ]

alpha_length = len(alpha)

grid = int(input(f"Before we start playiing,\nEnter how many grids you would like to play on\n Pick a number between 5 and {alpha_length}: "))


for x in range(grid):
    board.append(alpha[x] * grid)
    for number in range(len(board)):
            if number == 0:
                index = 1
                board[number] = str(index)
                index +=1
    


def board_print(board):
    for row in board:
        print(f"{0} ".join(row))
        

        




board_print(board)