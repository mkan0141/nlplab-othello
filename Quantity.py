import numpy as np

class Quantity():
    def __init__(self):
        self.default_q = 1
        self.value = {}
        self.eta = 0.3
        self.ganma = 0.9


    def get(self, state, action):
        state = [j for i in state.board for j in i]
        _value = self.value.get((tuple(state), tuple(action)))
        # print('_value; {}'.format(_value if _value is not None else self.default_q))
        return _value if _value is not None else self.default_q

    def set(self, state, action, quantity):
        state = [j for i in state.board for j in i]
        self.value[(tuple(state), tuple(action))] = quantity


    def update(self, state, action, reward, max_q):
        nq = self.get(state, action)
        new_q = nq + self.eta * ((reward +self.ganma * max_q) - nq)
        # print('new quantity: {}'.format(new_q))
        self.set(state, action, new_q)


