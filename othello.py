# import numpy as np
import tkinter as tk
import threading
import time
import argparse
import os
import sys
import pickle

import board as B
import player as P
import AI as R
import GUI as G
import QLearning as Q

parser = argparse.ArgumentParser()
parser.add_argument("--p1",
                    help="先手を指定してください. 人間が打ちたい場合は1, ランダムAIの場合は2,  Q-learning AI は3を入力してください.",
                    type=int)
parser.add_argument("--p2",
                    help="後手を指定してください. 人間が打ちたい場合は1, ランダムAIの場合は2,  Q-learning AI は3を入力してください.",
                    type=int)

NONE  = 0
BLACK = 1
WHITE = 2

def set_player(args, color, s):
    if args is 1:
        _players = P.Player()
    elif args is 2:
        _players = R.RandomAI()
    elif args is 3:
        # 学習したデータがあればそれを読み込む
        if os.path.exists('./data/{}_move_4x4.pickle'.format(s)):
            with open('./data/{}_move_4x4.pickle'.format(s), 'rb') as f:
                print('ローディング中... ( 思った以上に時間がかかります )')
                _players = pickle.load(f)
                print('完了!!')
        else:
            _players = Q.QLearning(color)
    return _players


def turn(board, player, opponent_player, GUI, count):
        # 打てる場所のリストを作成
        color = board.get_color()
        valid_pos = board.get_valid_position(color)
        # 打つ場所がなかったらパスする
        if board.is_pass(valid_pos):
            if board.is_interruption():
                return "game-set"
            board.next_turn()
            board._pass = True
            return "pass"
        # どこに置くかを決定する
        x, y = player.move(board, color, GUI)
        # 盤面をひっくり返す
        board.reverse(color, x, y)
        board.next_turn()
        # Q-learning時にパラメータを更新する
        # player.getGameResult(board, opponent_player, GUI)

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

def game():
    # 各playerにインスタンスをセット
    args = parser.parse_args()
    player1 = set_player(args.p1, WHITE, 'first')
    player2 = set_player(args.p2, BLACK, 'second')

    board = B.Board()
    color = WHITE
    GUI.set_message("平研３回生　Othello")
    count = 0
    board.init()
    GUI.show_board(board.board)

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
        # playerの入力
        if color == BLACK:
            status = turn(board, player1, player2, GUI, count)
        else:
            status = turn(board, player2, player1, GUI, count)
        if status == "game-set":
            break
        GUI.show_board(board.board)
        time.sleep(1)

    GUI.show_board(board.get_board())
    GUI.set_message(str(board.who_won()))
    GUI.user_input()
    GUI.set_message("Thank you for playing!")
    time.sleep(2)
    GUI.close()


if __name__ == '__main__':
    args = parser.parse_args()
    if not ((1 <=args.p1 <= 3) & (1<= args.p2 <= 3)):
        print('引数で指定できる数字は1, 2, 3のみです.')
        sys.exit()

    p1 = set_player(args.p1, WHITE, 'first')
    p2 = set_player(args.p2, BLACK, 'second')

    root = tk.Tk()
    GUI = G.othello_GUI(master=root)
    thread = threading.Thread(target=game)
    thread.setDaemon(True)
    thread.start()
    GUI.mainloop()
