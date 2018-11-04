from Quantity import Quantity
from board import Board
from copy import deepcopy, copy
import AI as A

import random

class QLearning():
    def __init__(self, color):
        self.quantity = Quantity()
        self.action = None
        self.board = None
        self.color = color
        self.e = 0.2
        self.action_count = 0

    def move(self, board, color, GUI):
        return self.policy(board, color)


    def policy(self, _board, color):
        self.board = deepcopy(_board)
        valid_positions = self.board.get_valid_position(self.board.get_color())

        if len(valid_positions) == 0:
            return 'pass', 'pass'

        if random.random() < (self.e / (self.action_count // 10000 + 1)):
            self.action = random.choice(valid_positions)
        else:
            state = [j for i in self.board.board for j in i]
            # print(state)
            q_list = [self.quantity.get(state, position) for position in valid_positions]
            # print('q_list: {}'.format(q_list))
            q_max = max(q_list)

            best_index = [i for i in range(len(q_list)) if q_list[i] == q_max]
            best_index = random.choice(best_index)

            self.action = valid_positions[best_index]
        # print('q-player ({},{})'.format(x, y))
        return self.action


    def getGameResult(self, _board, opponent_player, GUI):
        board = deepcopy(_board)
        # print(board.get_color())
        # print('stone_nunm2: {}'.format(board.stone_num))
        # print('color: {}'.format(board.color))
        x, y = opponent_player.move(board, board.get_color(), 0)

        if x != 'pass':
            # print('reverse')
            board.reverse(board.get_color(), x, y)
        """
        print('2--------------')
        board.show_board()
        print('--------------')
        """
        reward = 0
        # print('stone_nunm3: {}'.format(board.stone_num))
        if board.is_end():
            #print('iiiiiiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnnnnnnn')
            reward = (1 if board.who_won() == self.color else -1)
        """
        if reward != 0:
            print(reward)
        """
        # print('reward: {}'.format(reward))

        if self.board != None:
            self.learn(self.board, self.action, reward, board)

        if not board.is_end():
            self.action_count += 1
            self.board = None
            self.action = None


    def learn(self, state, action, reward, board):
        valid_positions = board.get_valid_position(self.color)

        state = [j for i in state.board for j in i]
        board = [j for i in board.board for j in i]

        pQ = self.quantity.get(state, action)

        q_list = [self.quantity.get(board, position) for position in valid_positions]

        if len(q_list) == 0:
            q_max = 0
        else:
            q_max = max(q_list)

        # print(q_max)
        self.quantity.update(state, action, reward, q_max)

