import random

class RandomAI:
    def random_ai(self, list):
        n = random.randrange(len(list))
        x = list[n][0]
        y = list[n][1]
        return x,y

