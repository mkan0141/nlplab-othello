import numpy as np

NONE  = 0
BLACK = 1
WHITE = 2

def init():
    board = [[NONE for i in range(8)]for j in range(8)]
    board[3][3] = board[4][4] = WHITE
    board[4][3] = board[3][4] = BLACK
    return board






"""
下のmain関数は
デバッグなどに使ってください.
"""
def main():
    board = init()


# これより下はいじらない
if __name__ == '__main__':
    main()
