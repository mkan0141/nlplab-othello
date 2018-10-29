import random
from board import Board

class RandomAI:
    def move(self, board, color):
        return self.random_ai(board, color)

    def random_ai(self, board, color):
        list = board.get_valid_position(color)
        if len(list) == 0:
            return 'pass', 'pass'
        # print(list)
        n = random.randrange(len(list))
        x = list[n][0]
        y = list[n][1]
        # print('random-player ({},{})'.format(x, y))
        return x, y

    def getGameResult(self, board, opponent_player):
        pass

