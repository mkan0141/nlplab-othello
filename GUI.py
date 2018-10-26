import tkinter as tk
from tkinter import messagebox
import threading
import time

NONE = 0 # 石が置かれていないマス
BLACK = 1 # 黒石が置かれているマス
WHITE = 2 # 白石が置かれているマス

# 盤の枠線の左上の座標 x1, y2, 右下の座標 x2, y2 を格納した辞書型配列
F = {"x1":50, "y1":50, "x2":450, "y2":450}
# マスのサイズ
MAS_SIZE = (F["x2"] - F["x1"]) / 8 

class othello_GUI(tk.Frame):
    def init(self):
        # ウィンドウの作成
        self.canvas = tk.Canvas(self, bg="white", height=500, width=650)
        # 盤の作成
        self.canvas.create_rectangle(F["x1"], F["y1"], F["x2"], F["y2"], fill="green")
        for i in range(7):
            i += 1
            x, y = F["x1"] + i * 50, F["y1"] + i * 50
            self.canvas.create_line(x, F["y1"], x, F["y2"])
            self.canvas.create_line(F["x1"], y, F["x2"], y)
        f = ('Century', '13', 'bold')
        # 盤の座標表記
        for i in range(8):
            self.canvas.create_text(F["x1"]+25+50*i, F["y1"]-12, font=f, text=chr(i+ord('a')))
            self.canvas.create_text(F["x1"]-12, F["y1"]+25+50*i, font=f, text=i+1)
        # 盤に描かれてる謎の黒丸4つ
        for a, b in [[2,2], [2,6], [6,2], [6,6]]:
            self.canvas.create_oval(F["x1"]+50*a-3, F["y1"]+50*b-3, F["x1"]+50*a+3, F["y1"]+50*b+3, fill="black")
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.master.protocol("WM_DELETE_WINDOW", self._close_message)
        self.mouse_activate = False
        self.mouse_clicked = False
        self.mouse_x, self.mouse_y = 0, 0
        self.close_flag = False
        self.canvas.pack()

    def __init__(self, master=None):
        super().__init__(master)
        master.title("Othello")
        self.pack()
        self.init()

    def mouse_click(self, e):
        if self.mouse_activate:
            self.mouse_clicked = True
            self.mouse_x, self.mouse_y = e.x, e.y
        
    def get_mouse(self):
        self.mouse_activate = True
        while True:
            if self.mouse_clicked:
                self.mouse_clicked = False
                return self._board_position(self.mouse_x, self.mouse_y)

    def change__board_position(self, x, y):
        x = (x - F["x1"]) // MAS_SIZE
        y = (y - F["y1"]) // MAS_SIZE
        return x, y

    def show_board(self, board):
        for y in range(8):
            for x in range(8):
                x1, y1 = self._canvas_position(x, y)
                self.canvas.create_oval(x1 - 21, y1 - 21, x1 + 21, y1 + 21, fill="green", outline="green")
                if board[y][x] == BLACK:
                    self.canvas.create_oval(x1 - 20, y1 - 20, x1 + 20, y1 + 20, fill="black")
                elif board[y][x] == WHITE:
                    self.canvas.create_oval(x1 - 20, y1 - 20, x1 + 20, y1 + 20, fill="white")
        self.canvas.update()

    def _canvas_position(self, x, y):
        return F["x1"] + 25 + 50 * x, F["y1"] + 25 + 50 * y 

    def _board_position(self, x, y):
        return x // F["x1"], y // F["y1"]

    def close(self):
        self.master.destroy()

    def _close_message(self):
        if self.close_flag:
            self.close()
        else:
            messagebox.showinfo("error message", "メインプログラムが終了していません。")

    def can_close(self):
        self.close_flag = True

def game():
    board = [[NONE for i in range(8)]for j in range(8)]
    board[3][3] = board[4][4] = WHITE
    board[4][3] = board[3][4] = BLACK
    test.show_board(board)
    board[4][5] = WHITE
    time.sleep(1)
    test.show_board(board)
    time.sleep(1)
    board[4][5] = NONE
    test.show_board(board)
    while True:
        x, y = test.get_mouse()
        print(x, y)
        if x == 1 and y == 1:
            break
    test.can_close()

if __name__=='__main__':   
    root = tk.Tk()
    test = othello_GUI(master=root)
    b = threading.Thread(target=game)
    b.start()
    test.mainloop()