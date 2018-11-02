import numpy as np
import board as B
import player as P
import AI as R
import Naive as N
import QLearning as Q

import pickle
import os
import matplotlib.pyplot as plt

NONE  = 0
BLACK = 1
WHITE = 2


def turn(board, player, opponent_player, GUI):
        # print('stone_nunm1: {}'.format(board.stone_num))
        # 打てる場所のリストを作成
        valid_pos = board.get_valid_position(board.get_color())

        # 打つ場所がなかったらパスする
        if board.is_pass(valid_pos):
            if board.is_interruption():
                return "game-set"
            board.next_turn()
            board._pass = True
            return "pass"

        # 打てる場所を出力
        # print(valid_pos)
        # ユーザからの入力
        x, y = player.move(board, board.get_color(), 0)
        #print('({}, {})'.format(x, y))
        # player.getGameResult(board, opponent_player)
        # x, y = random_ai.random_ai(valid_pos)
        # ひっくり返す

        board.reverse(board.get_color(), x, y)
        # print('1--------------')
        # board.show_board()
        board.next_turn()
        # print('--------------')
        player.getGameResult(board, opponent_player, 0)


def game(player1, player2):
    if type(player1) == Q.QLearning:
        if os.path.exists('./data/first_win_rate.pickle'):
            with open('./data/first_win_rate.pickle', 'rb') as f:
                win_rate = pickle.load(f)
        else:
            win_rate = []

    if type(player2) == Q.QLearning:
        if os.path.exists('./data/first_win_rate.pickle'):
            with open('./data/second_win_rate.pickle', 'rb') as f:
                win_rate = pickle.load(f)
        else:
            win_rate = []
    b = 0
    w = 0
    cnt = 1

    board = B.Board()
    player = P.Player()
    random_ai = R.RandomAI()
    color = BLACK
    while True:
        for i in range(100):
            w = 0
            b = 0
            for j in range(100):
                board.init()
                while not board.is_end():
                    color = board.get_color()
                    if color == BLACK:
                        status = turn(board, player1, player2, 0)
                    else:
                        status = turn(board, player2, player1, 0)
                    if status == "game-set":
                        break
                    # 盤面の表示
                    # print('after -------------->')
                    # board.show_board()

                win = board.who_won()
                if win == BLACK:
                    # print('black win')
                    b += 1
                elif win == WHITE:
                    # print('white win')
                    w += 1

            if type(player1) == Q.QLearning:
                win_rate.append(b / 100)
            else:
                win_rate.append(w / 100)

            print('black {} win'.format(b))
            print('white {} win'.format(w))

        if type(player1) == Q.QLearning:
            with open('./data/first_move_4x4.pickle'.format(cnt), 'wb') as f:
                pickle.dump(player1, f)
            with open('./data/first_win_rate.pickle', 'wb') as f:
                pickle.dump(win_rate, f)

        if type(player2) == Q.QLearning:
            with open('./data/second_move_4x4.pickle', 'wb') as f:
                pickle.dump(player2, f)
            with open('./data/second_win_rate.pickle', 'wb') as f:
                pickle.dump(win_rate, f)

        cnt += 1
        # plt.plot(win_rate)
        # plt.show()



if __name__ == '__main__':
    x = 3 #int(input('先手: ナイーブ=1, ランダム=2, QL=3  > '))
    if x is 1:
        player1 = N.NaiveAI()
    elif x is 2:
        player1 = R.RandomAI()
    elif x is 3:
        if os.path.exists('./data/first_move.pickle'):
            with open('./data/first_move.pickle', 'rb') as f:
                player1 = pickle.load(f)
        else:
            player1 = Q.QLearning(BLACK)


    x = 2 #int(input('後手: ナイーブ=1, ランダム=2, QL=3  > '))
    if x is 1:
        player2 = N.NaiveAI()
    elif x is 2:
        player2 = R.RandomAI()
    elif x is 3:
        if os.path.exists('./data/second_move.pickle'):
            with open('./data/second_move.pickle', 'rb') as f:
                player2 = pickle.load(f)
        else:
            player2 = Q.QLearning(WHITE)

    game(player1, player2)

