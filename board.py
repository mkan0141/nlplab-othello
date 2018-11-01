import numpy as np

NONE  = 0
BLACK = 1
WHITE = 2
BOARD_SIZE = 8
BOARD_HARF_SIZE = int(BOARD_SIZE / 2)
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

class Board():

    def __init__(self):
        self.board = [[NONE for i in range(BOARD_SIZE)]for j in range(BOARD_SIZE)]
        self.turn = 0
        self.stone_num = 4
        self.is_slip = False
        self.color = BLACK
        self._pass = False
        self.interruption = False


    def init(self):
        self.board = [[NONE for i in range(BOARD_SIZE)]for j in range(BOARD_SIZE)]
        self.board[BOARD_HARF_SIZE - 1][BOARD_HARF_SIZE - 1] = self.board[BOARD_HARF_SIZE ][BOARD_HARF_SIZE] = WHITE
        self.board[BOARD_HARF_SIZE][BOARD_HARF_SIZE - 1] = self.board[BOARD_HARF_SIZE - 1][BOARD_HARF_SIZE] = BLACK
        self.turn = 0
        self.stone_num = 4
        self.color = BLACK
        self._pass = False
        self.interruption = False
        self.valid_pos = []

    def next_turn(self):
        if self.color == WHITE:
            self.color = BLACK
        else:
            self.color = WHITE
        self.turn += 1

    def is_pass(self, valid_pos):
        if self._pass and len(valid_pos) == 0:
            self.interruption = True
        self._pass = len(valid_pos) == 0
        return self._pass

    def is_interruption(self):
        return self.interruption

    def whiteblack(self, x):
        return WHITE if x==BLACK else BLACK


    def get_color(self):
        return self.color

    def is_end(self):
        # print(self.stone_num)
        pos = self.get_valid_position(self.get_color())

        #x44x4print(self._pass and len(pos) == 0)
        return self.stone_num == BOARD_SIZE * BOARD_SIZE or (self._pass and len(pos) == 0)

    # 盤面を表示する関数です.
    def show_board(self):
        print("  A B C D E F G H")
        x = -1
        y = 0
        while y < BOARD_SIZE:
            while x < BOARD_SIZE:
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
        if x == 'pass':
            self._pass = True
            return
        self.stone_num += 1
        self._pass = False

        if color == WHITE:
            self.board[x][y] = WHITE

            y1 = y - 1
            while y1 + 1 > 0:
                if self.board[x][y1] == NONE:
                    y1 = -1
                elif self.board[x][y1] == WHITE:
                    y2 = y1 + 1
                    y1 = -1
                    while y2 < y:
                        self.board[x][y2] = WHITE
                        y2 += 1
                y1 -= 1
            y1 = y + 1
            while y1 - 1 < BOARD_SIZE - 1:
                if self.board[x][y1] == NONE:
                    y1 = BOARD_SIZE - 1
                elif self.board[x][y1] == WHITE:
                    y2 = y1 - 1
                    y1 = BOARD_SIZE - 1
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
            while x1 - 1 < BOARD_SIZE - 1:
                if self.board[x1][y] == NONE:
                    x1 = BOARD_SIZE - 1
                elif self.board[x1][y] == WHITE:
                    x2 = x1 - 1
                    x1 = BOARD_SIZE - 1
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
            while x1 - 1 < BOARD_SIZE - 1 and y1 - 1 < BOARD_SIZE - 1:
                if self.board[x1][y1] == NONE:
                    x1 = BOARD_SIZE - 1
                elif self.board[x1][y1] == WHITE:
                    x2 = x1 - 1
                    y2 = y1 - 1
                    x1 = BOARD_SIZE - 1
                    while x2 > x:
                        self.board[x2][y2] = WHITE
                        x2 -= 1
                        y2 -= 1
                x1 += 1
                y1 += 1

            x1 = x - 1
            y1 = y + 1
            while x1 + 1 > 0 and y1 - 1 < BOARD_SIZE - 1:
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
            while x1 - 1 < BOARD_SIZE - 1 and y1 + 1 > 0:
                if self.board[x1][y1] == NONE:
                    x1 = BOARD_SIZE - 1
                elif self.board[x1][y1] == WHITE:
                    x2 = x1 - 1
                    y2 = y1 + 1
                    x1 = BOARD_SIZE - 1
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
            while y1 - 1 < BOARD_SIZE - 1:
                if self.board[x][y1] == NONE:
                    y1 = BOARD_SIZE - 1
                elif self.board[x][y1] == BLACK:
                    y2 = y1 - 1
                    y1 = BOARD_SIZE - 1
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
            while x1 - 1 < BOARD_SIZE - 1:
                if self.board[x1][y] == NONE:
                    x1 = BOARD_SIZE - 1
                elif self.board[x1][y] == BLACK:
                    x2 = x1 - 1
                    x1 = BOARD_SIZE - 1
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
            while x1 - 1 < BOARD_SIZE - 1 and y1 - 1 < BOARD_SIZE - 1:
                if self.board[x1][y1] == NONE:
                    x1 = BOARD_SIZE - 1
                elif self.board[x1][y1] == BLACK:
                    x2 = x1 - 1
                    y2 = y1 - 1
                    x1 = BOARD_SIZE - 1
                    while x2 > x:
                        self.board[x2][y2] = BLACK
                        x2 -= 1
                        y2 -= 1
                x1 += 1
                y1 += 1

            x1 = x - 1
            y1 = y + 1
            while x1 + 1 > 0 and y1 - 1 < BOARD_SIZE - 1:
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
            while x1 - 1 < BOARD_SIZE - 1 and y1 + 1 > 0:
                if self.board[x1][y1] == NONE:
                    x1 = BOARD_SIZE - 1
                elif self.board[x1][y1] == BLACK:
                    x2 = x1 - 1
                    y2 = y1 + 1
                    x1 = BOARD_SIZE - 1
                    while x2 > x:
                        self.board[x2][y2] = BLACK
                        x2 -= 1
                        y2 += 1
                x1 += 1
                y1 -= 1









    #置ける場所リスト
    def ayasi(self, x, y, color):
        aitecolor = self.whiteblack(color)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < BOARD_SIZE and ny >= 0 and ny < BOARD_SIZE and self.board[ny][nx] == aitecolor:
                return True
        return False

    def check(self, x, y, color):
        aitecolor = self.whiteblack(color)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < BOARD_SIZE and ny >= 0 and ny < BOARD_SIZE and self.board[ny][nx] == aitecolor:
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    if nx >=0 and nx < BOARD_SIZE and ny >= 0 and ny < BOARD_SIZE and self.board[ny][nx] == aitecolor:
                        continue
                    elif nx >=0 and nx < BOARD_SIZE and ny >= 0 and ny < BOARD_SIZE and self.board[ny][nx] == color:
                        return True
                    else:
                        break
        return False


    def get_valid_position(self, color):
        list = []
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if not self.board[y][x] == NONE:
                    continue
                if self.ayasi(x, y, color) == True:
                    if self.check(x, y, color) == True:
                        list.append([x,y])
        return list

    def who_won(self):
        x = 0
        y = 0
        w = 0
        b = 0

        while y < BOARD_SIZE:
            while x < BOARD_SIZE:
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
            self.is_win = NONE

    def get_board(self):
        return self.board