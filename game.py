import numpy as np
import board as B
import player as P
import AI as R

NONE  = 0
BLACK = 1
WHITE = 2

def game():
    board = B.Board()
    player = P.Player()
    random_ai = R.RandomAI()
    color = WHITE

    board.init()
    while not board.is_end():
        # print(board.is_end())
        color = board.get_color()
        # 盤面の表示
        board.show_board()
        # 打てる場所のリストを作成
        valid_pos = board.get_valid_position(color)
        # 打つ場所がなかったらパスする
        if board.is_pass(valid_pos):
            if board.is_interruption():
                break
            board.next_turn()
            continue
        # 打てる場所を出力
        player.show_valid_position(valid_pos)
        # ユーザからの入力
        y, x = player.user_input(valid_pos)
        # x, y = random_ai.random_ai(valid_pos)
        # ひっくり返す
        board.reverse(color, x, y)
        board.next_turn()

    print(board.who_won())



if __name__ == '__main__':
    game()

