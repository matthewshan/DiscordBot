import random

colors = ['red', 'yellow', 'green', 'blue', 'purple', 'pink']

class Move:
    def __init__(self, color1, color2, color3, color4):
        self.order = []
        self.order[0] = color1
        self.order[1] = color2
        self.order[2] = color3
        self.order[3] = color4


class Game:
    def __init__(self):
        self.ongoing = False
        self.turnCount = 0
        self.answer = Move(random.choice(colors), random.choice(colors),
                           random.choice(colors), random.choice(colors), )
    def guess(self, color1, color2, color3, color4):
        blackpegs = 0
        whitepegs = 0
        move = Move(color1, color2, color3, color4)
        if move.order[0] == color1:
            blackpegs += 1
        if move.order[1] == color2:
            blackpegs += 1
        if move.order[2] == color3:
            blackpegs += 1
        if move.order[3] == color4:
            blackpegs += 1
        for x in self.answer.order:
            if move.order[0] ==


