



import numpy as np

board = np.array([
[[0],[0],[0]],
[[0],[0],[0]],
[[0],[0],[0]],
], dtype=object)


def print_board(board):
    for i in range(3):
        print("\n")
        for j in range(3):
            print(board[i][j][0], end='|')
    return None

def x_turn(column, row):
    if board[row, column, 0] == 0:
        board[row, column, 0] = "X"
        print_board(board)
        print("\n")
    else:
        if board[row, column, 0] == "X":
          return "That spot is already occupied by you!"
        elif board[row, column, 0] == "Y":
          return "That spot is already occupied by the opponent!"


def y_turn(column, row):
    if board[row, column, 0] == 0:
        board[row, column, 0] = "Y"
        print_board(board)
        print("\n")

    else:
        if board[row, column, 0] == "Y":
            return "That spot is already occupied by you!"
        elif board[row, column, 0] == "X":
            return "That spot is already occupied by the opponent!"


def check_line(line):
    try:
     if (line == ["X", "X", "X"]):
        return "X"
     elif (line == ["Y", "Y", "Y"]):
            return "Y"
     else:
        return None
    except Exception as e:
        print(f"An error occured!! {e}!!")


def check(board):
    for i in range(3):
        check_board = []
        for j in range(3):
            value = board[i][j][0]
            check_board.append(value)
        response = check_line(check_board)
        if response:
            return response

    for i in range(3):
            check_board = []
            for j in range(3):
                value = board[j][i][0]
                check_board.append(value)
            response = check_line(check_board)
            if response:
                return response


    response = check_line([board[0][0], board[1][1], board[2][2]])
    if response:
        return response
    else:
        response = check_line([board[0][2], board[1][1], board[2][0]])
        if response:
            return response


def x_input():
    try:
      x_col = int(input("This is player X's turn, please enter the column (vertical) you wanna place the X on: "))
      x_row = int(input("This is player X's turn, please enter the row (horizontal) you wanna place the X on: "))
      return x_turn(x_col - 1, x_row - 1)
    except Exception as e:
        print(f"An error occured!! {e}!!")

def y_input():
    try:
        y_col = int(input("This is player Y's turn, please enter the column (vertical) you wanna place the Y on: "))
        y_row = int(input("This is player Y's turn, please enter the row (horizontal) you wanna place the Y on: "))
        return y_turn(y_col - 1, y_row - 1)
    except Exception as e:
        print(f"An error occured!! {e}!!")



print_board(board)
print("\n")
while check(board) == None:
    try:
        response = x_input()
        while response != None:
            print(response)
            response = x_input()
        if check(board) == None:
            response = y_input()
            while response != None:
                print(response)
                response = y_input()
        else:
            break
    except Exception as e:
        print(f"An error occured!! {e}!!")







if check(board) == "X":
    print("X has won!")
elif check(board) == "Y":
    print("Y has won!")
else:
    print("Yo you got a bug here")







