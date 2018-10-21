import numpy as np

NONE  = 0
BLACK = 1
WHITE = 2

def init():
    board = [[NONE for i in range(8)]for j in range(8)]
    board[3][3] = board[4][4] = WHITE
    board[4][3] = board[3][4] = BLACK
    return board

# 盤面を表示する関数です.
def show_board(board):
    print("  A B C D E F G H")
    x = -1
    y = 0
    while y < 8:
        while x < 8:
            if x == -1:
                print(y+1, end="")
            else:
                if board[x][y] == NONE:
                    print(" .", end="")
                elif board[x][y] == WHITE:
                    print(" o", end="") 
                elif board[x][y] == BLACK:
                    print(" x", end="")               
            x += 1
        x = -1
        y += 1
        print()
        
# 石をひっくり返す処理

    
        
"""
下のmain関数は
デバッグなどに使ってください.
"""
def main():
    board = init()


# これより下はいじらない
if __name__ == '__main__':
    main()
