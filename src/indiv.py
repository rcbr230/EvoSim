
import random
from Genome import Genome
from NeuralNet import NeuralNet
"""
alive
age
genome
nnet - this is what uses the genome
reponsiveness
last move direction

"""
class indiv:
    
    def __init__(self, loc_:tuple, index_:int):
        self.alive = True
        self.index = index_
        self.loc = loc_
        self.age = 0
        self.nnet = NeuralNet()
        self.lastMoveDir = random.randint(0,3) # 0-up, 1-right, 2-down, 3-left
        g = Genome()
        g.makeRandomGenome()
        self.genome = g
        self.genome.createWiring()

    def isAlive(self):
        return self.alive
    
    # use nnet to generate actions, and perform them
    def feedForward(self, simStep):
        actions = list()
        neuronOutputsDone = False

        return actions
        