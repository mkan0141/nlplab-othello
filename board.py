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

def reverse(color, x, y, board):

    if color == WHITE:
        board[x][y] = WHITE

        y1 = y - 1
        while y1 + 1 > 0:
            if board[x][y1] == NONE: 
                y1 = -1           
            elif board[x][y1] == WHITE:
                y2 = y1 + 1
                y1 = -1
                while y2 < y:
                    board[x][y2] = WHITE
                    y2 += 1
            y1 -= 1
        y1 = y + 1
        while y1 - 1 < 7:
            if board[x][y1] == NONE:
                y1 = 7
            elif board[x][y1] == WHITE:
                y2 = y1 - 1
                y1 = 7
                while y2 > y:
                    board[x][y2] = WHITE
                    y2 -= 1
            y1 += 1

        x1 = x - 1
        while x1 + 1 > 0:
            if board[x1][y] == NONE: 
                x1 = -1  
            elif board[x1][y] == WHITE:
                x2 = x1 + 1
                x1 = -1
                while x2 < x:
                    board[x2][y] = WHITE
                    x2 += 1
            x1 -= 1 
        x1 = x + 1
        while x1 - 1 < 7:
            if board[x1][y] == NONE: 
                x1 = 7              
            elif board[x1][y] == WHITE:
                x2 = x1 - 1
                x1 = 7
                while x2 > x:
                    board[x2][y] = WHITE
                    x2 -= 1
            x1 += 1

        x1 = x - 1
        y1 = y - 1
        while x1 + 1 > 0 and y1 + 1 > 0:
            if board[x1][y1] == NONE: 
                x1 = -1
            elif board[x1][y1] == WHITE:
                x2 = x1 + 1
                y2 = y1 + 1
                x1 = -1
                while x2 < x:
                    board[x2][y2] = WHITE
                    x2 += 1
                    y2 += 1
            x1 -= 1
            y1 -= 1 
        x1 = x + 1
        y1 = y + 1
        while x1 - 1 < 7 and y1 - 1 < 7:
            if board[x1][y1] == NONE: 
                x1 = 7
            elif board[x1][y1] == WHITE:
                x2 = x1 - 1
                y2 = y1 - 1
                x1 = 7
                while x2 > x:
                    board[x2][y2] = WHITE
                    x2 -= 1
                    y2 -= 1
            x1 += 1
            y1 += 1
        
        x1 = x - 1
        y1 = y + 1
        while x1 + 1 > 0 and y1 - 1 < 7:
            if board[x1][y1] == NONE: 
                x1 = -1
            elif board[x1][y1] == WHITE:
                x2 = x1 + 1
                y2 = y1 - 1
                x1 = -1
                while x2 < x:
                    board[x2][y2] = WHITE
                    x2 += 1
                    y2 -= 1
            x1 -= 1
            y1 += 1 
        x1 = x + 1
        y1 = y - 1
        while x1 - 1 < 7 and y1 + 1 > 0:
            if board[x1][y1] == NONE: 
                x1 = 7
            elif board[x1][y1] == WHITE:
                x2 = x1 - 1
                y2 = y1 + 1
                x1 = 7
                while x2 > x:
                    board[x2][y2] = WHITE
                    x2 -= 1
                    y2 += 1
            x1 += 1
            y1 -= 1


    elif color == BLACK:
        board[x][y] = BLACK

        y1 = y - 1
        while y1 + 1 > 0:
            if board[x][y1] == NONE: 
                y1 = -1           
            elif board[x][y1] == BLACK:
                y2 = y1 + 1
                y1 = -1
                while y2 < y:
                    board[x][y2] = BLACK
                    y2 += 1
            y1 -= 1
        y1 = y + 1
        while y1 - 1 < 7:
            if board[x][y1] == NONE:
                y1 = 7
            elif board[x][y1] == BLACK:
                y2 = y1 - 1
                y1 = 7
                while y2 > y:
                    board[x][y2] = BLACK
                    y2 -= 1
            y1 += 1

        x1 = x - 1
        while x1 + 1 > 0:
            if board[x1][y] == NONE: 
                x1 = -1  
            elif board[x1][y] == BLACK:
                x2 = x1 + 1
                x1 = -1
                while x2 < x:
                    board[x2][y] = BLACK
                    x2 += 1
            x1 -= 1 
        x1 = x + 1
        while x1 - 1 < 7:
            if board[x1][y] == NONE: 
                x1 = 7              
            elif board[x1][y] == BLACK:
                x2 = x1 - 1
                x1 = 7
                while x2 > x:
                    board[x2][y] = BLACK
                    x2 -= 1
            x1 += 1

        x1 = x - 1
        y1 = y - 1
        while x1 + 1 > 0 and y1 + 1 > 0:
            if board[x1][y1] == NONE: 
                x1 = -1
            elif board[x1][y1] == BLACK:
                x2 = x1 + 1
                y2 = y1 + 1
                x1 = -1
                while x2 < x:
                    board[x2][y2] = BLACK
                    x2 += 1
                    y2 += 1
            x1 -= 1
            y1 -= 1 
        x1 = x + 1
        y1 = y + 1
        while x1 - 1 < 7 and y1 - 1 < 7:
            if board[x1][y1] == NONE: 
                x1 = 7
            elif board[x1][y1] == BLACK:
                x2 = x1 - 1
                y2 = y1 - 1
                x1 = 7
                while x2 > x:
                    board[x2][y2] = BLACK
                    x2 -= 1
                    y2 -= 1
            x1 += 1
            y1 += 1
        
        x1 = x - 1
        y1 = y + 1
        while x1 + 1 > 0 and y1 - 1 < 7:
            if board[x1][y1] == NONE: 
                x1 = -1
            elif board[x1][y1] == BLACK:
                x2 = x1 + 1
                y2 = y1 - 1
                x1 = -1
                while x2 < x:
                    board[x2][y2] = BLACK
                    x2 += 1
                    y2 -= 1
            x1 -= 1
            y1 += 1 
        x1 = x + 1
        y1 = y - 1
        while x1 - 1 < 7 and y1 + 1 > 0:
            if board[x1][y1] == NONE: 
                x1 = 7
            elif board[x1][y1] == BLACK:
                x2 = x1 - 1
                y2 = y1 + 1
                x1 = 7
                while x2 > x:
                    board[x2][y2] = BLACK
                    x2 -= 1
                    y2 += 1
            x1 += 1
            y1 -= 1

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
