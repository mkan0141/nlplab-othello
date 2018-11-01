import tkinter as tk
from tkinter import messagebox
import threading
import time

NONE = 0 # 石が置かれていないマス
BLACK = 1 # 黒石が置かれているマス
WHITE = 2 # 白石が置かれているマス

# マスのサイズ
MAS_SIZE = 50
# ボードのサイズ〇x〇
BOARD_SIZE = 8
# ボードの中心
CENTER = [250, 270]
# 盤の枠線の左上の座標 x1, y2, 右下の座標 x2, y2 を格納した辞書型配列
F = {"x1":CENTER[0]-BOARD_SIZE*MAS_SIZE/2, "y1":CENTER[1]-BOARD_SIZE*MAS_SIZE/2, "x2":CENTER[0]+BOARD_SIZE*MAS_SIZE/2, "y2":CENTER[1]-BOARD_SIZE*MAS_SIZE/2}
# 駒の半径
STONE_SIZE = 20
# 盤の色
BG_COLOR = "green"
# 変化したときの盤の色
SD_COLOR = "lightgreen"
# マウスカーソル上のマスの色
M_COLOR = "aquamarine"

class othello_GUI(tk.Frame):
    """ 念のために、 _ から始まる名前のメソッドは参照しないでください。 """
    def _init(self):
        # ウィンドウの枠組みを作る
        self.main_frame = tk.Frame(self, height=500, width=650)
        self.main_frame.pack()
        self.text_frame = tk.Frame(self.main_frame, height=40, width=650)
        self.text_frame.pack(side=tk.BOTTOM)
        self.list_frame = tk.Frame(self.main_frame, height=500, width=60)
        self.list_frame.pack(side=tk.RIGHT)

        # キャンバスの作成
        self.canvas = tk.Canvas(self.main_frame, height=500, width=500)

        # オセロのロゴ
        f = ('MV Boli', '20', 'underline')
        self.canvas.create_text(325, 30, font=f, text="Othello")

        # 盤の作成
        self.mas = [[0 for i in range(BOARD_SIZE)]for j in range(BOARD_SIZE)]
        self.stone = [[0 for i in range(BOARD_SIZE)]for j in range(BOARD_SIZE)]
        color = BG_COLOR
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                x1, y1, = F["x1"] + j * MAS_SIZE, F["y1"] + i * MAS_SIZE
                x2, y2 = x1 + MAS_SIZE, y1 + MAS_SIZE
                self.mas[i][j] = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                x1, y1 = self._canvas_position(j, i)
                self.stone[i][j] = self.canvas.create_oval(x1 - STONE_SIZE, y1 - STONE_SIZE, x1 + STONE_SIZE, y1 + STONE_SIZE, fill=color, outline=color)
        
        # 盤の座標表記
        f = ('Century', '13', 'bold')
        for i in range(BOARD_SIZE):
            self.canvas.create_text(F["x1"]+MAS_SIZE/2+MAS_SIZE*i, F["y1"]-12, font=f, text=chr(i+ord('a')))
            self.canvas.create_text(F["x1"]-12, F["y1"]+MAS_SIZE/2+MAS_SIZE*i, font=f, text=i+1)
        
        # 盤に描かれてる謎の黒丸4つ
        if BOARD_SIZE == 8:
            for a, b in [[2,2], [2,6], [6,2], [6,6]]:
                self.canvas.create_oval(F["x1"]+MAS_SIZE*a-3, F["y1"]+MAS_SIZE*b-3, F["x1"]+MAS_SIZE*a+3, F["y1"]+MAS_SIZE*b+3, fill="black")
        
        # 左クリックで呼ぶメソッドの設定
        self.canvas.bind("<Button-1>", self._mouse_click)
        self.mouse_activate = False
        self.mouse_clicked = False
        self.mouse_x, self.mouse_y = 0, 0

        self.canvas.bind("<Motion>", self._mouse_move)
        self.lmouse = [0, 0, BG_COLOR]

        # ウィンドウを閉じようとしたときに呼ぶメソッドの設定
        self.master.protocol("WM_DELETE_WINDOW", self._close_message)

        # ウィンドウ下部にテキストを表示する枠を用意
        self.msg = tk.StringVar()
        f = ('ＭＳ明朝', '10', 'bold')
        self.label = tk.Label(self.text_frame, textvariable=self.msg, font=f, relief="sunken", width=70)
        self.msg.set("ここにメッセージが表示される。")

        # スクロールバー付きのリストボックスを作成する。
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT,fill="y")
        self.list_box = tk.Listbox(self.list_frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list_box.yview)

        # キャンバス、リストボックス、ラベルをウィンドウに取り付ける。
        self.canvas.pack(side=tk.LEFT)
        self.list_box.pack(side=tk.LEFT)
        self.label.pack(side=tk.BOTTOM)

    def __init__(self, master=None):
        # スーパークラスの__init__を呼ぶ
        super().__init__(master)
        # タイトル
        master.title("Othello")
        self.pack()
        self._init()

    def _mouse_click(self, e):
        # マウスがクリックされた時の処理
        if self.mouse_activate:
            self.mouse_clicked = True
            self.mouse_x, self.mouse_y = e.x, e.y
    
    def _mouse_move(self, e):
        # マウスが動いたときの処理
        if 0 <= self.lmouse[0] < BOARD_SIZE and 0 <= self.lmouse[1] < BOARD_SIZE:
            # 色を変えていたマスの色を戻す。
            self._set_bgcolor(self.lmouse[1], self.lmouse[0], self.lmouse[2])
        x, y = self._board_position(e.x, e.y)
        if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
            # マウスカーソル上のマスの色を変える。
            self.lmouse = [x, y, self.canvas.itemcget(self.mas[y][x], "fill")]
            self._set_bgcolor(y, x, M_COLOR)

    def user_input(self):
        """このメソッドを呼んでから左クリックをしたときの座標をボードのマス目基準で返却する。
        ただし、返却される座標はそれぞれ 1 ~ BOARD_SIZE の間とは限らない。"""
        self.mouse_activate = True
        while True:
            time.sleep(0.1)
            if self.mouse_clicked:
                self.mouse_clicked = False
                return self._board_position(self.mouse_x, self.mouse_y)

    def _board_position(self, x, y):
        # キャンバス上での座標をボードのマス基準の座標に変換する。
        x = (x - F["x1"]) // MAS_SIZE
        y = (y - F["y1"]) // MAS_SIZE
        return int(x), int(y)

    def _canvas_position(self, x, y):
        # マス基準の座標をキャンバス上におけるそのマスの中心値に変換する。
        x = F["x1"] + MAS_SIZE/2 + MAS_SIZE * x
        y = F["y1"] + MAS_SIZE/2 + MAS_SIZE * y 
        return x, y

    def _allset_bgcolor(self, color):
        # マスの色をすべてcolorにする。
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if [self.lmouse[0], self.lmouse[1]] == [j, i]:
                    self.lmouse[2] = BG_COLOR
                self._set_bgcolor(i, j, color)

    def _set_bgcolor(self, y, x, color):
        # (x, y)のマスの色をcolorにする。
        self.canvas.itemconfigure(self.mas[y][x], fill=color)
        if self.canvas.itemcget(self.stone[y][x], "outline") != "black": # 白黒どちらでもoutlineは黒
            self.canvas.itemconfigure(self.stone[y][x], fill=color, outline=color) 

    def show_board(self, board):
        # ボードの石の状況を表示する。
        self._allset_bgcolor(BG_COLOR)
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if board[x][y] == BLACK:
                    self.canvas.itemconfigure(self.stone[x][y], fill="black", outline="black")
                elif board[x][y] == WHITE:
                    self.canvas.itemconfigure(self.stone[x][y], fill="white", outline="black")
                    
              
    def close(self):
        # ウィンドウを閉じる。
        self.master.destroy()

    def _close_message(self):
        # ウィンドウを閉じようとしたときに呼ばれるメソッド。
        if messagebox.askokcancel("Message", "プログラムを終了します。"):
            self.closed = True
            self.close()

    def clean_board(self):
        """ボードを何もない状態にする。"""
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.canvas.itemconfigure(self.mas[i][j], fill=BG_COLOR)
                self.canvas.itemconfigure(self.stone[i][j], fill=BG_COLOR, outline=BG_COLOR)

    def set_message(self, msg):
        """ウィンドウ下部に表示したい文章を入力する。クラス名.set_message("ここにメッセージを入力する。")"""
        self.msg.set(msg)

    def show_valid_position(self, valid_pos):
        """石がおけるマスの色を変える。引数に「置ける場所リスト」を指定する。"""
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if [x, y] in valid_pos:
                    if [self.lmouse[0], self.lmouse[1]] in valid_pos:
                        self.lmouse[2] = SD_COLOR
                    self._set_bgcolor(y, x, SD_COLOR)
        
    def append_list(self, text):
        """リストの末尾に要素textを追加する。"""
        self.list_box.insert(tk.END, text)
        self.list_box.yview_scroll(1, "units")

    def del_list(self):
        """リストの要素をすべて消す。"""
        self.list_box.delete(0, tk.END)

def game():
    board = [[NONE for i in range(BOARD_SIZE)]for j in range(BOARD_SIZE)]
    board[3][3] = board[4][4] = WHITE
    board[4][3] = board[3][4] = BLACK
    # 石の表示を更新する。
    test.show_board(board)
    board[4][5] = WHITE
    # リストにテキストを追加する。
    for i in range(20):
        test.append_list("test"+str(i))
    #time.sleep(1) # 1秒待つ
    # 石の表示を更新する。
    test.show_board(board)
    # メッセージの表示を更新する。
    test.set_message("ここにメッセージを入力する。")
    #time.sleep(1)
    board[1][1] = BLACK
    # 石の表示を更新する。
    test.show_board(board)
    pos = [[1,1], [2,3], [BOARD_SIZE, 5],[2,4]]
    # 置ける場所の表示を更新する。
    test.show_valid_position(pos)
    # マウス入力を待つ。
    x, y = test.user_input()
    # get_mouse()で返却される値。
    print(x, y)
    test.user_input()
    # リストの内容をすべて消去する。
    test.del_list()
    # ボードの石をすべて消す。
    test.clean_board()

    # ウィンドウを閉じる
    test.close()

if __name__=='__main__':
    root = tk.Tk()
    test = othello_GUI(master=root)
    thread = threading.Thread(target=game)
    thread.setDaemon(True)
    thread.start()
    test.mainloop()