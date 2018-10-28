import numpy as np
import board as B
import player as P
import AI as R
import Naive as N
import QLearning as Q
import matplotlib.pyplot as plt

NONE  = 0
BLACK = 1
WHITE = 2


win_rate = []

def turn(board, player, opponent_player):
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
        x, y = player.move(board, board.get_color())
        #print('({}, {})'.format(x, y))
        # player.getGameResult(board, opponent_player)
        # x, y = random_ai.random_ai(valid_pos)
        # ひっくり返す
        
        board.reverse(board.get_color(), x, y)
        # print('1--------------')
        # board.show_board()
        board.next_turn()
        # print('--------------')
        player.getGameResult(board, opponent_player)
        

def game(player1, player2):
    b = 0
    w = 0
    board = B.Board()
    player = P.Player()
    random_ai = R.RandomAI()
    color = WHITE
    for i in range(50):
        w = 0
        b = 0 
        for j in range(100):
            board.init()
            while not board.is_end():
                color = board.get_color()
                if color == WHITE:
                    status = turn(board, player1, player2)
                else:
                    status = turn(board, player2, player1)
                
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
            else:
                print('even')
        win_rate.append(w / 100)
        print('white {} win'.format(w))
        print('black {} win'.format(b))
    plt.plot(win_rate)
    plt.show()
    


if __name__ == '__main__':
    x = int(input('先手: ナイーブ=1, ランダム=2, QL=3  > '))
    if x is 1:
        player1 = N.NaiveAI()
    elif x is 2:
        player1 = R.RandomAI()
    elif x is 3:
        player1 = Q.QLearning(WHITE)


    x = int(input('後手: ナイーブ=1, ランダム=2, QL=3  > '))
    if x is 1:
        player2 = N.NaiveAI()
    elif x is 2:
        player2 = R.RandomAI()
    elif x is 3:
        player2 = Q.QLearning(BLACK)

    game(player1, player2)

