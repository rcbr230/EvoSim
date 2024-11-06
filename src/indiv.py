
import math
import random
from Genome import Genome
from NeuralNet import NeuralNet
from enum import Enum
from enum import auto
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

class SensoryValues(Enum):
    Age = 0
    Rnd = 1
    Blr = 2
    Osc = 3
    Bfd = 4
    Plr = 5
    Pop = 6
    Pfd = 7
    LPf = 8
    LMy = 9
    LBf = 10
    LMx = 11
    BDy = 12
    Gen = 13
    BDx = 14
    Lx =  15
    BD =  16
    Ly =  17

class indiv:
    TOTAL_SENSORY  = 18
    TOTAL_INTERNAL = 6
    TOTAL_ACTION   = 6
    def __init__(self, loc_:tuple, index_:int):
        print(SensoryValues.Age.value)
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


        # stores as:
            # index is the sensor node. If the size > 0 then it exists
            # holds a (type, connection)
                # type = NodeVal.Internal or NodeVal.Action
                # connection is the index for actionOutputs
        self.sensoryConnections = self.getSensoryNodes() # generate a connection list for all sensory nodes
        self.InternalConnections = self.getInternalNodes()
        self.sensoryValues = []*self.TOTAL_SENSORY
        self.actionOutputs = []*self.TOTAL_ACTION
        # GENERATE NEURAL NET FROM THE GENOME CREATED

    def getSensoryNodes(self):
        ret = [[] for _ in range(self.TOTAL_SENSORY)]
        for i in self.genome.GenomeList:
            if i.sourceType == 0:
                index = i.sourceNum % self.TOTAL_SENSORY
                conn = 0
                type = NodeVal.Internal
                if i.sinkType == 0:
                    conn = i.sinkNum % self.TOTAL_INTERNAL
                    type = NodeVal.Internal
                else:
                    conn = i.sinkNum % self.TOTAL_ACTION
                    type = NodeVal.Action
                sensorConn = (type,conn)
                ret[index].append(sensorConn)
        return ret
    

    def getInternalNodes(self):
        ret = [[] for _ in range(self.TOTAL_INTERNAL)]
        for i in self.genome.GenomeList:
            if i.sourceType == 1:
                index = i.sourceNum % self.TOTAL_INTERNAL
                conn = 0
                type = NodeVal.Internal
                if i.sinkType == 0:
                    conn = i.sinkNum % self.TOTAL_INTERNAL
                    type = NodeVal.Internal
                else:
                    conn = i.sinkNum % self.TOTAL_ACTION
                    type = NodeVal.Action
                sensorConn = (type,conn)
                ret[index].append(sensorConn)
        # end will hold the output
        return ret
    
    def sumInternalFromSensory(self):
        pass
    
    def sumActionFromSensory(self):
        pass
    
    def sumInternalFromInternal(self):
        pass
    
    def isAlive(self):
        return self.alive
    
    # use nnet to generate actions, and perform them
    def feedForward(self, simStep, grid):
        pass

    
