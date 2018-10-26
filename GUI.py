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
# 駒の半径
STONE_SIZE = 20
# 盤の色
BD_COLOR = "green"
# 変化したときの盤の色
SD_COLOR = "lightgreen"

class othello_GUI(tk.Frame):
    def init(self):
        # ウィンドウの作成
        self.canvas = tk.Canvas(self, bg="white", height=500, width=650)

        # 盤の作成
        self.mas = [[0 for i in range(8)]for j in range(8)]
        self.stone = [[0 for i in range(8)]for j in range(8)]
        color = BD_COLOR
        for i in range(8):
            for j in range(8):
                x1, y1, = F["x1"] + j * MAS_SIZE, F["y1"] + i * MAS_SIZE
                x2, y2 = x1 + MAS_SIZE, y1 + MAS_SIZE
                self.mas[i][j] = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                x1, y1 = self._canvas_position(j, i)
                self.stone[i][j] = self.canvas.create_oval(x1 - STONE_SIZE, y1 - STONE_SIZE, x1 + STONE_SIZE, y1 + STONE_SIZE, fill=color, outline=color)
        
        # 盤の座標表記
        f = ('Century', '13', 'bold')
        for i in range(8):
            self.canvas.create_text(F["x1"]+MAS_SIZE/2+MAS_SIZE*i, F["y1"]-12, font=f, text=chr(i+ord('a')))
            self.canvas.create_text(F["x1"]-12, F["y1"]+MAS_SIZE/2+MAS_SIZE*i, font=f, text=i+1)
        
        # 盤に描かれてる謎の黒丸4つ
        for a, b in [[2,2], [2,6], [6,2], [6,6]]:
            self.canvas.create_oval(F["x1"]+MAS_SIZE*a-3, F["y1"]+MAS_SIZE*b-3, F["x1"]+MAS_SIZE*a+3, F["y1"]+MAS_SIZE*b+3, fill="black")
        
        # 左クリックで呼ぶメソッドの設定
        self.canvas.bind("<Button-1>", self._mouse_click)
        self.mouse_activate = False
        self.mouse_clicked = False
        self.mouse_x, self.mouse_y = 0, 0

        # ウィンドウを閉じようとしたときに呼ぶメソッドの設定
        self.master.protocol("WM_DELETE_WINDOW", self._close_message)
        self.close_flag = False

        # ウィンドウ下部にテキストを表示する枠を用意
        self.msg = tk.StringVar()
        f = ('ＭＳ明朝', '10', 'bold')
        self.label = tk.Label(self.master, textvariable=self.msg, font=f)
        self.msg.set("ここにメッセージが表示される。")

        self.canvas.pack()
        self.label.pack(side=tk.BOTTOM)

    def __init__(self, master=None):
        # スーパークラスの__init__を呼ぶ
        super().__init__(master)
        # タイトル
        master.title("Othello")
        self.pack()
        self.init()

    def _mouse_click(self, e):
        # マウスがクリックされた時の処理
        if self.mouse_activate:
            self.mouse_clicked = True
            self.mouse_x, self.mouse_y = e.x, e.y
        
    def get_mouse(self):
        """このメソッドを呼んでから左クリックをしたときの座標をボードのマス目基準で返却する。
        ただし、返却される座標はそれぞれ1~8の間とは限らない。
        """
        self.mouse_activate = True
        while True:
            if self.mouse_clicked:
                self.mouse_clicked = False
                return self._board_position(self.mouse_x, self.mouse_y)

    def _board_position(self, x, y):
        # キャンバス上での座標をボードのマス基準の座標に変換する。
        x = (x - F["x1"]) // MAS_SIZE + 1
        y = (y - F["y1"]) // MAS_SIZE + 1
        return int(x), int(y)

    def _canvas_position(self, x, y):
        # マス基準の座標をキャンバス上におけるそのマスの中心値に変換する。
        x = F["x1"] + MAS_SIZE/2 + MAS_SIZE * x
        y = F["y1"] + MAS_SIZE/2 + MAS_SIZE * y 
        return x, y

    def _allset_bgcolor(self, color):
        # マスの色をすべてcolorにする。
        for i in range(8):
            for j in range(8):
                self._set_bgcolor(i, j, color)

    def _set_bgcolor(self, y, x, color):
        # (x, y)のマスの色をcolorにする。
        self.canvas.itemconfigure(self.mas[y][x], fill=color)
        if self.canvas.itemcget(self.stone[y][x], "outline") != "black": # 白黒どちらでもoutlineは黒
            self.canvas.itemconfigure(self.stone[y][x], fill=color, outline=color) 

    def show_board(self, board):
        # ボードの石の状況を表示する。
        self._allset_bgcolor(BD_COLOR)
        for y in range(8):
            for x in range(8):
                if board[y][x] == BLACK:
                    self.canvas.itemconfigure(self.stone[y][x], fill="black", outline="black")
                elif board[y][x] == WHITE:
                    self.canvas.itemconfigure(self.stone[y][x], fill="white", outline="black")
                    
              
    def _close(self):
        # ウィンドウを閉じる。
        self.master.destroy()

    def _close_message(self):
        # ウィンドウを閉じようとしたときに呼ばれるメソッド。通常状態では閉じれない。
        if self.close_flag:
            self._close()
        else:
            messagebox.showinfo("error message", "メインプログラムが終了していません。")

    def closable(self):
        # ウィンドウを閉じれるようにする。
        self.close_flag = True

    def set_message(self, msg):
        """ウィンドウ下部に表示したい文章を入力する。クラス名.set_message("ここにメッセージを入力する。")"""
        self.msg.set(msg)

    def show_put(self, valid_pos):
        """石がおけるマスの色を変える。引数に「置ける場所リスト」を指定する。"""
        for y in range(8):
            for x in range(8):
                if [x+1, y+1] in valid_pos:
                    self._set_bgcolor(y, x, SD_COLOR)
        

def game():
    board = [[NONE for i in range(8)]for j in range(8)]
    board[3][3] = board[4][4] = WHITE
    board[4][3] = board[3][4] = BLACK
    # 石の表示を更新する。
    test.show_board(board)
    board[4][5] = WHITE
    time.sleep(1) # 1秒待つ
    # 石の表示を更新する。
    test.show_board(board)
    # メッセージの表示を更新する。
    test.set_message("ここにメッセージを入力する。")
    time.sleep(1)
    board[4][5] = NONE
    # 石の表示を更新する。
    test.show_board(board)
    pos = [[1,1], [3,3], [8, 5]]
    # 置ける場所の表示を更新する。
    test.show_put(pos)
    # マウス入力を待つ。
    x, y = test.get_mouse()
    print(x, y)

    # ウィンドウを閉じられるようにする。
    test.closable()

if __name__=='__main__':   
    root = tk.Tk()
    test = othello_GUI(master=root)
    thread = threading.Thread(target=game)
    thread.start()
    test.mainloop()