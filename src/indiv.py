
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
        self.internalNodes = [0]*6
        self.actionNodes = {
            "LPD" : 0,
            "OSC" : 0,
            "Res" : 0,
            "Mfd" : 0,
            "Mrn" : 0,
            "Mrv" : 0,
            "MRL" : 0,
            "MX" : 0,
            "MY" : 0
        }

    def isAlive(self):
        return self.alive
    
    # use nnet to generate actions, and perform them
    def feedForward(self, simStep, grid):
        actions = list()
        neuronOutputsDone = False

        # compute actions using genome here!
        
        self.GenSensoryInputs(grid)
        return actions
    
    def GenSensoryInputs(self, grid):
        pass