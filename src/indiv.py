
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
        self.sensoryConnections,self.sensoryWeights = self.getSensoryNodes() # generate a connection list for all sensory nodes
        self.internalConnections, self.internalWeights = self.getInternalNodes()

        self.sensoryValues = []*self.TOTAL_SENSORY
        self.internalOutputs = [0]*self.TOTAL_INTERNAL
        self.actionOutputs = [0]*self.TOTAL_ACTION
        # GENERATE NEURAL NET FROM THE GENOME CREATED

    def getSensoryNodes(self):
        connections = [[] for _ in range(self.TOTAL_SENSORY)]
        weights = []*self.TOTAL_SENSORY

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
                connections[index].append(sensorConn)
                weights[index] = i.weight
        return connections,weights
    

    def getInternalNodes(self):
        connections = [[] for _ in range(self.TOTAL_INTERNAL)]
        weights = []*self.TOTAL_INTERNAL

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
                internalConn = (type,conn)
                connections[index].append(internalConn)
                weights[index] = i.weight
        # end will hold the output
        return connections,weights
    

    def genSensoryData(self,grid,age):
        # Age = age
        if len(self.sensoryConnections[0]) != 0:
            self.sensoryValues[0] = age

        # Rnd = random input
        if len(self.sensoryConnections[1]) != 0:
            self.sensoryValues[1] = random.randint(0,1000)

        # Blr = blockage left-right
        if len(self.sensoryConnections[2]) != 0:    
            if self.lastMoveDir == 0 or self.lastMoveDir == 2:
                left = self.loc[0]-1
                right = self.loc[0]+1
                if left > 0:
                    self.sensoryValues[2] = grid.gridInfo[left][self.loc[1]]
                if right < grid.sizeX:
                    self.sensoryValues[2] = grid.gridInfo[right][self.loc[1]]
            else:
                left = self.loc[1]-1
                right = self.loc[1]+1
                if left > 0:
                    self.sensoryValues[2] = grid.gridInfo[self.loc[0]][left]
                if right < grid.sizeY:
                    self.sensoryValues[2] = grid.gridInfo[self.loc[1]][right]     
        if self.sensoryValues[2] > 0:
            self.sensoryValues[2] = 1

        # Osc = oscillator
        if len(self.sensoryConnections[3]) != 0:
            self.curOsc = not self.curOsc
            self.sensoryValues[3] = self.curOsc

        # Bfd = blockage forward
        if len(self.sensoryConnections[4]) != 0:
            if self.lastMoveDir == 0:
                front = self.loc[1]+1
                if front > 0:
                    self.sensoryValues[4] = grid.gridInfo[front][self.loc[1]]
            elif self.lastMoveDir == 1:
                front = self.loc[0]+1
                if front > 0:
                    self.sensoryValues[4] = grid.gridInfo[self.loc[0]][front]
            elif self.lastMoveDir == 2:
                front = self.loc[1]-1
                if front > 0:
                    self.sensoryValues[4] = grid.gridInfo[front][self.loc[1]]
            elif self.lastMoveDir == 3:
                front = self.loc[1]-1
                if front > 0:
                    self.sensoryValues[4] = grid.gridInfo[self.loc[0]][front]
            if self.sensoryValues[4] > 0:
                self.sensoryValues[4] = 1

                                                                # Plr = population gradient left-right
        if len(self.sensoryConnections[5]) != 0:
            pass
                                                                # Pop = population density
        if len(self.sensoryConnections[6]) != 0:
            pass
                                                                # Pfd = population gradient forward
        if len(self.sensoryConnections[7]) != 0:
            pass
                                                                # LPf = population long-range forward
        if len(self.sensoryConnections[8]) != 0:
            pass
        # LMy = last movement Y
        if len(self.sensoryConnections[9]) != 0:
            if self.lastMoveDir == 0 or self.lastMoveDir == 2:
                self.sensoryValues[9] = 0
            else:
                self.sensoryValues[9] += 1

                                                                # LBf = blockage long-range forward
        if len(self.sensoryConnections[10]) != 0:
            pass
        # LMx = last movement X
        if len(self.sensoryConnections[11]) != 0:
            if self.lastMoveDir == 1 or self.lastMoveDir == 3:
                self.sensoryValues[11] = 0
            else:
                self.sensoryValues[11] += 1

        # BDy = north/south border distance
        if len(self.sensoryConnections[12]) != 0:
            self.sensoryValues[12] = min(self.loc[1], grid.sizeY-self.loc[1])

                                                                # Gen = genetic similarity of forward neighbor 
        if len(self.sensoryConnections[13]) != 0:
            pass
        
        # BDx = east/west border distance
        if len(self.sensoryConnections[14]) != 0:
            self.sensoryValues[14] = min(self.loc[0], grid.sizeX-self.loc[0])
        
        # Lx = east/west world location
        if len(self.sensoryConnections[15]) != 0:
            self.sensoryValues[15] = self.loc[0]

        # BD = nearest border distance
        if len(self.sensoryConnections[16]) != 0:
            xDist = min(self.loc[0], grid.sizeX-self.loc[0])
            yDist = min(self.loc[1], grid.sizeY-self.loc[1])
            self.sensoryValues[16] = min(xDist,yDist)
            
        # Ly = north/south world location
        if len(self.sensoryConnections[17]) != 0:
            self.sensoryValues[17] = self.loc[1]
        

    # Run in this order!------------------------------------------------------------------------------------------------
    def sumInternalFromSensory(self):
        for i in range(len(self.sensoryConnections)):
            for connection in self.sensoryConnections[i]:
                if connection[0] == NodeVal.Internal:
                    self.internalOutputs[connection[1]] += self.sensoryValues[i] * self.sensoryWeights[i]
    
    def sumInternalFromInternal(self):
        for i in range(len(self.internalConnections)):
            for connection in self.internalConnections[i]:
                if connection[0] == NodeVal.Internal:
                    self.internalOutputs[connection[1]] += self.internalOutputs[i] * self.internalWeights[i]

    def sumActionFromSensory(self):
        for i in range(len(self.sensoryConnections)):
            for connection in self.sensoryConnections[i]:
                if connection[0] == NodeVal.Action:
                    self.actionOutputs[connection[1]] += self.sensoryValues[i] * self.sensoryWeights[i]
    
    def sumActionFromInternal(self):
        for i in range(len(self.internalConnections)):
            for connection in self.sensoryConnections[i]:
                if connection[0] == NodeVal.Action:
                    self.actionOutputs[connection[1]] += self.internalOutputs[i] * self.internalWeights[i]
    # -------------------------------------------------------------------------------------------------------------------

    def InternalTanH(self):
        for i in range(len(self.internalOutputs)):
            self.internalOutputs[i] = math.tanh(self.internalOutputs[i])

    def ActionTanH(self):
        for i in range(len(self.actionOutputs)):
            self.actionOutputs[i] = math.tanh(self.actionOutputs[i])     

    def isAlive(self):
        return self.alive
    
    # use nnet to generate actions, and perform them
    def feedForward(self, simStep, grid):
        self.genSensoryData(grid,simStep)
        self.sumInternalFromSensory()
        self.sumActionFromSensory()

        self.InternalTanH()

        self.sumInternalFromInternal()       
        self.sumActionFromInternal()

        self.ActionTanH()

        self.runActions()

    
