import random
from board import Board

class NaiveAI:
    def move(self, board, color):
        return self.naive_ai(board, color)

    def naive_ai(self, board, color):
        list = board.get_valid_position(color)
        x = list[0][0]
        y = list[0][1]
        return x,y

    def getGameResult(self, board, opponent_player):
        pass

