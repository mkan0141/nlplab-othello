# import numpy as np
import board as B
import player as P
import AI as R
import GUI as G
import tkinter as tk
import threading
import time

NONE  = 0
BLACK = 1
WHITE = 2

def game():
    board = B.Board()
    # player = P.Player()
    # random_ai = R.RandomAI()
    color = WHITE
    GUI.set_message("平研３回生　Othello")
    count = 0
    GUI.user_input()
    board.init()
    while not board.is_end():
        # print(board.is_end())
        color = board.get_color()
        count += 1
        # 盤面の表示
        GUI.show_board(board.get_board())
        # 打てる場所のリストを作成
        valid_pos = board.get_valid_position(color)
        # 打つ場所がなかったらパスする
        if board.is_pass(valid_pos):
            if board.is_interruption():
                break
            board.next_turn()
            continue
        # 打てる場所を出力
        GUI.show_valid_position(valid_pos)
        # ユーザからの入力
        GUI.set_message("置きたい場所をクリックしてください.")
        x, y = GUI.user_input()
        while [x, y] not in valid_pos:
            GUI.set_message("その場所には置けません...")
            x, y = GUI.user_input()

        # x, y = random_ai.random_ai(valid_pos)

        # 棋譜を追加する。
        msg = str(count) + " : "
        if count < 10:
            msg = " " + msg     # 1~9のとき、空白を入れる
        if color == BLACK:
            msg += "黒"
        else:
            msg += "白"
        msg += chr(ord("a")+x) + str(y+1)
        GUI.append_list(msg)
        
        # ひっくり返す
        board.reverse(color, x, y)
        board.next_turn()

    GUI.show_board(board.get_board())
    GUI.set_message(str(board.who_won()))
    GUI.user_input()
    GUI.set_message("Thank you for playing!")
    time.sleep(2)
    GUI.close()

if __name__ == '__main__':
    root = tk.Tk()
    GUI = G.othello_GUI(master=root)
    thread = threading.Thread(target=game)
    thread.setDaemon(True)
    thread.start()
    GUI.mainloop()
