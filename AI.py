import random

l = [[2, 3], [3, 2], [4, 5], [5, 4]]

def random_ai(list):
    n = random.randrange(len(list))
    x = list[n][0]
    y = list[n][1]

    #print(x,y)
    #print(list[n])

    return x,y


random_ai(l)