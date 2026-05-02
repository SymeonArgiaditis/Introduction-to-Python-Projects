from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        self.position = tuple(x + y for x,y in zip(self.position, move))
        
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def level_up(self):
        self.moves += [(1, 1), (1, -1), (-1, -1), (-1, 1)]

p = Pawn()
p.make_move()