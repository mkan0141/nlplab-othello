import numpy as np

NONE  = 0
BLACK = 1
WHITE = 2
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

class Board():
    def __init__(self):
        self.board = [[NONE for i in range(8)]for j in range(8)]


    def init(self):
        self.board = [[NONE for i in range(8)]for j in range(8)]
        self.board[3][3] = self.board[4][4] = WHITE
        self.board[4][3] = self.board[3][4] = BLACK

    # 盤面を表示する関数です.
    def show_board(self):
        print("  A B C D E F G H")
        x = -1
        y = 0
        while y < 8:
            while x < 8:
                if x == -1:
                    print(y+1, end="")
                else:
                    if self.board[y][x] == NONE:
                        print(" .", end="")
                    elif self.board[y][x] == WHITE:
                        print(" o", end="")
                    elif self.board[y][x] == BLACK:
                        print(" x", end="")
                x += 1
            x = -1
            y += 1
            print()

    # 石をひっくり返す処理

    def reverse(self, color, y, x):

        if color == WHITE:
            self.board[x][y] = WHITE

            y1 = y - 1
            while y1 + 1 > 0:
                if self.board[x][y1] == NONE:
                    iy1 = -1
                elif self.board[x][y1] == WHITE:
                    y2 = y1 + 1
                    y1 = -1
                    while y2 < y:
                        self.board[x][y2] = WHITE
                        y2 += 1
                y1 -= 1
            y1 = y + 1
            while y1 - 1 < 7:
                if self.board[x][y1] == NONE:
                    y1 = 7
                elif self.board[x][y1] == WHITE:
                    y2 = y1 - 1
                    y1 = 7
                    while y2 > y:
                        self.board[x][y2] = WHITE
                        y2 -= 1
                y1 += 1

            x1 = x - 1
            while x1 + 1 > 0:
                if self.board[x1][y] == NONE:
                    x1 = -1
                elif self.board[x1][y] == WHITE:
                    x2 = x1 + 1
                    x1 = -1
                    while x2 < x:
                        self.board[x2][y] = WHITE
                        x2 += 1
                x1 -= 1
            x1 = x + 1
            while x1 - 1 < 7:
                if self.board[x1][y] == NONE:
                    x1 = 7
                elif self.board[x1][y] == WHITE:
                    x2 = x1 - 1
                    x1 = 7
                    while x2 > x:
                        self.board[x2][y] = WHITE
                        x2 -= 1
                x1 += 1

            x1 = x - 1
            y1 = y - 1
            while x1 + 1 > 0 and y1 + 1 > 0:
                if self.board[x1][y1] == NONE:
                    x1 = -1
                elif self.board[x1][y1] == WHITE:
                    x2 = x1 + 1
                    y2 = y1 + 1
                    x1 = -1
                    while x2 < x:
                        self.board[x2][y2] = WHITE
                        x2 += 1
                        y2 += 1
                x1 -= 1
                y1 -= 1
            x1 = x + 1
            y1 = y + 1
            while x1 - 1 < 7 and y1 - 1 < 7:
                if self.board[x1][y1] == NONE:
                    x1 = 7
                elif self.board[x1][y1] == WHITE:
                    x2 = x1 - 1
                    y2 = y1 - 1
                    x1 = 7
                    while x2 > x:
                        self.board[x2][y2] = WHITE
                        x2 -= 1
                        y2 -= 1
                x1 += 1
                y1 += 1

            x1 = x - 1
            y1 = y + 1
            while x1 + 1 > 0 and y1 - 1 < 7:
                if self.board[x1][y1] == NONE:
                    x1 = -1
                elif self.board[x1][y1] == WHITE:
                    x2 = x1 + 1
                    y2 = y1 - 1
                    x1 = -1
                    while x2 < x:
                        self.board[x2][y2] = WHITE
                        x2 += 1
                        y2 -= 1
                x1 -= 1
                y1 += 1
            x1 = x + 1
            y1 = y - 1
            while x1 - 1 < 7 and y1 + 1 > 0:
                if self.board[x1][y1] == NONE:
                    x1 = 7
                elif self.board[x1][y1] == WHITE:
                    x2 = x1 - 1
                    y2 = y1 + 1
                    x1 = 7
                    while x2 > x:
                        self.board[x2][y2] = WHITE
                        x2 -= 1
                        y2 += 1
                x1 += 1
                y1 -= 1


        elif color == BLACK:
            self.board[x][y] = BLACK

            y1 = y - 1
            while y1 + 1 > 0:
                if self.board[x][y1] == NONE:
                    y1 = -1
                elif self.board[x][y1] == BLACK:
                    y2 = y1 + 1
                    y1 = -1
                    while y2 < y:
                        self.board[x][y2] = BLACK
                        y2 += 1
                y1 -= 1
            y1 = y + 1
            while y1 - 1 < 7:
                if self.board[x][y1] == NONE:
                    y1 = 7
                elif self.board[x][y1] == BLACK:
                    y2 = y1 - 1
                    y1 = 7
                    while y2 > y:
                        self.board[x][y2] = BLACK
                        y2 -= 1
                y1 += 1

            x1 = x - 1
            while x1 + 1 > 0:
                if self.board[x1][y] == NONE:
                    x1 = -1
                elif self.board[x1][y] == BLACK:
                    x2 = x1 + 1
                    x1 = -1

                    while x2 < x:
                        self.board[x2][y] = BLACK
                        x2 += 1
                x1 -= 1
            x1 = x + 1
            while x1 - 1 < 7:
                if self.board[x1][y] == NONE:
                    x1 = 7
                elif self.board[x1][y] == BLACK:
                    x2 = x1 - 1
                    x1 = 7
                    while x2 > x:
                        self.board[x2][y] = BLACK
                        x2 -= 1
                x1 += 1

            x1 = x - 1
            y1 = y - 1
            while x1 + 1 > 0 and y1 + 1 > 0:
                if self.board[x1][y1] == NONE:
                    x1 = -1
                elif self.board[x1][y1] == BLACK:
                    x2 = x1 + 1
                    y2 = y1 + 1
                    x1 = -1
                    while x2 < x:
                        self.board[x2][y2] = BLACK
                        x2 += 1
                        y2 += 1
                x1 -= 1
                y1 -= 1
            x1 = x + 1
            y1 = y + 1
            while x1 - 1 < 7 and y1 - 1 < 7:
                if self.board[x1][y1] == NONE:
                    x1 = 7
                elif self.board[x1][y1] == BLACK:
                    x2 = x1 - 1
                    y2 = y1 - 1
                    x1 = 7
                    while x2 > x:
                        self.board[x2][y2] = BLACK
                        x2 -= 1
                        y2 -= 1
                x1 += 1
                y1 += 1

            x1 = x - 1
            y1 = y + 1
            while x1 + 1 > 0 and y1 - 1 < 7:
                if self.board[x1][y1] == NONE:
                    x1 = -1
                elif self.board[x1][y1] == BLACK:
                    x2 = x1 + 1
                    y2 = y1 - 1
                    x1 = -1
                    while x2 < x:
                        self.board[x2][y2] = BLACK
                        x2 += 1
                        y2 -= 1
                x1 -= 1
                y1 += 1
            x1 = x + 1
            y1 = y - 1
            while x1 - 1 < 7 and y1 + 1 > 0:
                if self.board[x1][y1] == NONE:
                    x1 = 7
                elif self.board[x1][y1] == BLACK:
                    x2 = x1 - 1
                    y2 = y1 + 1
                    x1 = 7
                    while x2 > x:
                        self.board[x2][y2] = BLACK
                        x2 -= 1
                        y2 += 1
                x1 += 1
                y1 -= 1




    #置ける場所リスト
    def ayasi(self, x, y, color):
        aitecolor = NONE
        if color == BLACK:
            aitecolor = WHITE
        else:
            aitecolor = BLACK
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx <8 and ny >= 0 and ny <8 and self.board[ny][nx] == aitecolor:
                return True
        return False

    def check(self, x, y, color):
        aitecolor = NONE
        if color == BLACK:
            aitecolor = WHITE
        else:
            aitecolor = BLACK
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx <8 and ny >= 0 and ny <8 and self.board[ny][nx] == aitecolor:
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    if nx >=0 and nx <8 and ny >= 0 and ny <8 and self.board[ny][nx] == aitecolor:
                        continue
                    elif nx >=0 and nx <8 and ny >= 0 and ny <8 and self.board[ny][nx] == color:
                        return True
                    else:
                        break
        return False


    def get_valid_position(self, color):
        list = []
        for x in range(8):
            for y in range(8):
                if self.ayasi(x, y, color) == True:
                    if self.check(x, y, color) == True:
                        list.append([x,y])
        return list


    def who_won(self):
        x = 0
        y = 0
        w = 0
        b = 0

        while y < 8:
            while x < 8:
                if self.board[x][y] == WHITE:
                    w += 1
                elif self.board[x][y] == BLACK:
                    b += 1
                x += 1
            x = 0
            y += 1

        if w > b:
            return WHITE
        elif w < b:
            return BLACK
        elif w == b:
            return NONE

