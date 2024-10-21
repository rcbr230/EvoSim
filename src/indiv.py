
import random
from Genome import Genome
from NeuralNet import NeuralNet
from enum import Enum

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
    
class Action(Enum):
    MOVE_X=0,                    # W +- X component of movement
    MOVE_Y=1,                    # W +- Y component of movement
    MOVE_FORWARD=2,              # W continue last direction
    MOVE_RL=3,                   # W +- component of movement
    MOVE_RANDOM=4,               # W
    SET_OSCILLATOR_PERIOD=5,     # I
    SET_LONGPROBE_DIST=6,        # I
    SET_RESPONSIVENESS=7,        # I
    EMIT_SIGNAL0=8,              # W
    MOVE_EAST=9,                 # W
    MOVE_WEST=10,                # W
    MOVE_NORTH=11,               # W
    MOVE_SOUTH=12,               # W
    MOVE_LEFT=13,                # W
    MOVE_RIGHT=14,               # W
    MOVE_REVERSE=15,             # W
    NUM_ACTIONS=16,       # <<----------------- END OF ACTIVE ACTIONS MARKER

        