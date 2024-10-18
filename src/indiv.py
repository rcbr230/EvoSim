
import random
from Genome import Genome

"""
alive
age
genome
nnet - this is what uses the genome
reponsiveness
last move direction

"""
class indiv:
    
    def __init__(self, loc_:tuple):
        self.alive = True
        self.loc = loc_
        self.age = 0
        self.lastMoveDir = random.randint(0,3) # 0-up, 1-right, 2-down, 3-left
        g = Genome()
        g.makeRandomGenome()
        self.genome = g
        self.genome.createWiring()

    def isAlive(self):
        return self.alive
    
    # use nnet to generate actions, and perform them
    def runActions(self, simStep):
        pass