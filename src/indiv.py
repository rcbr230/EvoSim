
import math
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

sensory Inputs:
    Age = age
    Rnd = random input
    Blr = blockage left-right
    Osc = oscillator
    Bfd = blockage forward
    Plr = population gradient left-right
    Pop = population density
    Pfd = population gradient forward
    LPf = population long-range forward
    LMy = last movement Y
    LBf = blockage long-range forward
    LMx = last movement X
    BDy = north/south border distance
    Gen = genetic similarity of forward neighbor 
    BDx = east/west border distance
    Lx = east/west world location
    BD = nearest border distance
    Ly = north/south world location

    action
    LPD = set long-probe distance
    OSC = set oscillator period
    Res = set responsiveness
    Mfd = move forward
    Mrn = move random
    Mrv = move reverse
    MRL = move left/right (+/-)
    MX = move east/west (+/-)
    MY = move north/south (+/-)
"""
class NodeVal(Enum):
    Sensory  = 0
    Internal = 1
    Action   = 2

class indiv:
    
    def __init__(self, loc_:tuple, index_:int):
        self.alive = True
        self.index = index_
        self.loc = loc_
        self.age = 0
        self.curOsc = True
        self.nnet = NeuralNet()
        self.lastMoveDir = random.randint(0,3) # 0-up, 1-right, 2-down, 3-left
        g = Genome()
        g.makeRandomGenome()
        self.genome = g
        # self.genome.createWiring()
        self.sensoryInputs = {
            "Rnd" : "", 
            "Blr" : "",
            "Osc" : "",
            "Bfd" : "",
            "Plr" : "",
            "Pop" : "",
            "Pfd" : "",
            "LPf" : "",
            "LMy" : "",
            "LBf" : "",
            "LMx" : "",
            "BDy" : "",
            "Gen" : "",
            "BDx" : "",
            "Lx" : "",
            "BD" : "",
            "Ly" : ""
        }
        # GENERATE NEURAL NET FROM THE GENOME CREATED

    # CREATE FUNCtiON TO UPDATE SENSORY NODES
    def isAlive(self):
        return self.alive
    
    # use nnet to generate actions, and perform them
    def feedForward(self, simStep, grid):

        pass
    
