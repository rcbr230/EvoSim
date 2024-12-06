
import math
import random
import copy
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
    TOTAL_SENSORY  = 13
    TOTAL_INTERNAL = 6
    TOTAL_ACTION   = 8
    MAX_PROBE_DIST = 5
    PERFORM_ACTION = 0.2
    MUTATION_RATE = 1
    def __init__(self, loc_:tuple, index_:int, genome_):
        self.alive = True
        self.index = index_
        self.loc = loc_
        self.age = 0
        self.longProbeDist = 2
        self.curOsc = True
        self.nnet = NeuralNet()
        self.lastMoveDir = random.randint(0,3) # 0-up, 1-right, 2-down, 3-left
        g = Genome()
        if genome_ != 0:
            g = copy.deepcopy(genome_)
        else:
            g.makeRandomGenome()
        self.genome = g
        mutate = random.randint(0,100)
        if mutate < self.MUTATION_RATE:
            self.genome.randomMutation()
        # stores as:
            # index is the sensor node. If the size > 0 then it exists
            # holds a (type, connection)
                # type = NodeVal.Internal or NodeVal.Action
                # connection is the index for actionOutputs
        self.sensoryConnections,self.sensoryWeights = self.getSensoryNodes() # generate a connection list for all sensory nodes
        self.internalConnections, self.internalWeights = self.getInternalNodes()

        self.sensoryValues = [0]*self.TOTAL_SENSORY
        self.internalOutputs = [0]*self.TOTAL_INTERNAL
        self.actionOutputs = [0]*self.TOTAL_ACTION
        # GENERATE NEURAL NET FROM THE GENOME CREATED

    def isAlive(self):
        return self.alive
    
    def getGenome(self):
        return self.genome

    def getSensoryNodes(self):
        connections = [[] for _ in range(self.TOTAL_SENSORY)]
        weights = [0]*self.TOTAL_SENSORY

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
        weights = [0]*self.TOTAL_INTERNAL

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
                if front < grid.sizeY:
                    self.sensoryValues[4] = grid.gridInfo[front][self.loc[1]]
            elif self.lastMoveDir == 1:
                front = self.loc[0]+1
                if front < grid.sizeX:
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

        # LMy = last movement Y
        if len(self.sensoryConnections[5]) != 0:
            if self.lastMoveDir == 0 or self.lastMoveDir == 2:
                self.sensoryValues[5] = 0
            else:
                self.sensoryValues[5] += 1

                                                                # LBf = blockage long-range forward
        if len(self.sensoryConnections[6]) != 0:
            pass
        # LMx = last movement X
        if len(self.sensoryConnections[7]) != 0:
            if self.lastMoveDir == 1 or self.lastMoveDir == 3:
                self.sensoryValues[7] = 0
            else:
                self.sensoryValues[7] += 1

        # BDy = north/south border distance
        if len(self.sensoryConnections[8]) != 0:
            self.sensoryValues[8] = min(self.loc[1], grid.sizeY-self.loc[1])

        # BDx = east/west border distance
        if len(self.sensoryConnections[9]) != 0:
            self.sensoryValues[9] = min(self.loc[0], grid.sizeX-self.loc[0])
        
        # Lx = east/west world location
        if len(self.sensoryConnections[10]) != 0:
            self.sensoryValues[10] = self.loc[0]

        # BD = nearest border distance
        if len(self.sensoryConnections[11]) != 0:
            xDist = min(self.loc[0], grid.sizeX-self.loc[0])
            yDist = min(self.loc[1], grid.sizeY-self.loc[1])
            self.sensoryValues[11] = min(xDist,yDist)
            
        # Ly = north/south world location
        if len(self.sensoryConnections[12]) != 0:
            self.sensoryValues[12] = self.loc[1]
        

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
             

    def RunActions(self,grid):
        # LPD = set long-probe distance      change later maybe
        if self.actionOutputs[0] > self.PERFORM_ACTION:
            self.longProbeDist = self.actionOutputs[0] * self.MAX_PROBE_DIST
        # MvF = move forward
        if self.actionOutputs[1] > self.PERFORM_ACTION:    
            if self.lastMoveDir == 0:
                if self.loc[1] < grid.sizeY-1:
                    if grid.gridInfo[self.loc[0]][self.loc[1]+1] == 0:
                        newLoc = (self.loc[0],self.loc[1]+1)
                        if not grid.isOccupied(newLoc[0],newLoc[1]):
                            grid.updateIndex(self.loc,newLoc,self.index)
                            self.loc = newLoc
            elif self.lastMoveDir == 1:
                if self.loc[0] < grid.sizeX-1:
                    if grid.gridInfo[self.loc[0]+1][self.loc[1]] == 0:
                        newLoc = (self.loc[0]+1,self.loc[1])
                        if not grid.isOccupied(newLoc[0],newLoc[1]):
                            grid.updateIndex(self.loc,newLoc,self.index)
                            self.loc = newLoc
            elif self.lastMoveDir == 2:
                if self.loc[1] > 0:
                    if grid.gridInfo[self.loc[0]][self.loc[1]-1] == 0:
                        newLoc = (self.loc[0],self.loc[1]-1)
                        if not grid.isOccupied(newLoc[0],newLoc[1]):
                            grid.updateIndex(self.loc,newLoc,self.index)
                            self.loc = newLoc
            elif self.lastMoveDir == 3:
                if self.loc[0] > 0:
                    if grid.gridInfo[self.loc[0]-1][self.loc[1]] == 0:
                        newLoc = (self.loc[0]-1,self.loc[1])
                        if not grid.isOccupied(newLoc[0],newLoc[1]):
                            grid.updateIndex(self.loc,newLoc,self.index)
                            self.loc = newLoc
                  
        # Mrn = move random
        if self.actionOutputs[2] > self.PERFORM_ACTION:
            rX = random.randint(-1,1)
            rY = random.randint(-1,1)
            randX = self.loc[0]+rX
            randY = self.loc[1]+rY
            if randX < 0:
                randX = 0
            if randY < 0:
                randY = 0
            if randX >= grid.sizeX:
                randX = grid.sizeX-1
            if randY >= grid.sizeY:
                randY = grid.sizeY-1
            newLoc = (randX,randY)
            if not grid.isOccupied(newLoc[0],newLoc[1]):
                grid.updateIndex(self.loc,newLoc,self.index)
                self.loc = newLoc
        # Mrv = move reverse
        if self.actionOutputs[3] > self.PERFORM_ACTION:
            if self.lastMoveDir == 0:
                newLoc = (self.loc[0],max(0,self.loc[1]-1))
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.lastMoveDir = 2
                    self.loc = newLoc
            elif self.lastMoveDir == 1:
                newLoc = (max(0,self.loc[0]-1),self.loc[1])
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.lastMoveDir = 3
                    self.loc = newLoc
            elif self.lastMoveDir == 2:
                newLoc = (self.loc[0],min(grid.sizeY-1,self.loc[1]+1))
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.lastMoveDir = 0
                    self.loc = newLoc
            else:
                newLoc = (min(grid.sizeX-1,self.loc[0]+1),self.loc[1])
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.lastMoveDir = 1
                    self.loc = newLoc                              
        # MRL = move left/right (+/-)
        if self.actionOutputs[4] > self.PERFORM_ACTION:
            if self.actionOutputs[4] > self.PERFORM_ACTION + (1-self.PERFORM_ACTION)/10: # left
                if self.lastMoveDir == 0: 
                    newLoc = (max(0,self.loc[0]-1),self.loc[1])
                    if not grid.isOccupied(newLoc[0],newLoc[1]):
                        grid.updateIndex(self.loc,newLoc,self.index)
                        self.lastMoveDir = 3
                        self.loc = newLoc
                elif self.lastMoveDir == 1:
                    newLoc = (self.loc[0],min(self.loc[1]+1,grid.sizeY-1))
                    if not grid.isOccupied(newLoc[0],newLoc[1]):
                        grid.updateIndex(self.loc,newLoc,self.index)
                        self.lastMoveDir = 0
                        self.loc = newLoc
                elif self.lastMoveDir == 2:
                    newLoc = (min(grid.sizeX-1,self.loc[0]+1),self.loc[1])
                    if not grid.isOccupied(newLoc[0],newLoc[1]):
                        grid.updateIndex(self.loc,newLoc,self.index)
                        self.lastMoveDir = 1
                        self.loc = newLoc
                else:
                    newLoc = (self.loc[0],max(self.loc[1]-1,0))
                    if not grid.isOccupied(newLoc[0],newLoc[1]):
                        grid.updateIndex(self.loc,newLoc,self.index)
                        self.lastMoveDir = 2
                        self.loc = newLoc
            else:                                           # right
                if self.lastMoveDir == 0: 
                    newLoc = (min(grid.sizeX-1,self.loc[0]+1),self.loc[1])
                    if not grid.isOccupied(newLoc[0],newLoc[1]):
                        grid.updateIndex(self.loc,newLoc,self.index)
                        self.lastMoveDir = 1
                        self.loc = newLoc
                elif self.lastMoveDir == 1:
                    newLoc = (self.loc[0],max(self.loc[1]-1,0))
                    if not grid.isOccupied(newLoc[0],newLoc[1]):
                        grid.updateIndex(self.loc,newLoc,self.index)
                        self.lastMoveDir = 2
                        self.loc = newLoc
                elif self.lastMoveDir == 2:
                    newLoc = (max(0,self.loc[0]-1),self.loc[1])
                    if not grid.isOccupied(newLoc[0],newLoc[1]):
                        grid.updateIndex(self.loc,newLoc,self.index)
                        self.lastMoveDir = 3
                        self.loc = newLoc
                else:
                    newLoc = (self.loc[0],min(self.loc[1]+1,grid.sizeY-1))
                    if not grid.isOccupied(newLoc[0],newLoc[1]):
                        grid.updateIndex(self.loc,newLoc,self.index)
                        self.lastMoveDir = 0
                        self.loc = newLoc
    
        # MX = move east/west (+/-)
        if self.actionOutputs[5] > self.PERFORM_ACTION:
            if self.actionOutputs[5] > self.PERFORM_ACTION + (1-self.PERFORM_ACTION)/10: # west
                newX = self.loc[0]-1
                if newX < 0:
                    newX = 0
                newLoc = (newX,self.loc[1])
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.loc = newLoc
                    self.lastMoveDir = 3
            else:                           # east
                newX = self.loc[0]+1
                if newX >= grid.sizeX:
                    newX = grid.sizeX-1
                newLoc = (newX,self.loc[1])
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.loc = newLoc
                    self.lastMoveDir = 1

        
        # Mfd = move forward
        if self.actionOutputs[6] > self.PERFORM_ACTION:
            if self.lastMoveDir == 0:
                newLoc = (self.loc[0],min(self.loc[1]+1,grid.sizeY-1))
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.loc = newLoc
            elif self.lastMoveDir == 1:
                newLoc = (min(self.loc[0]+1, grid.sizeX-1),self.loc[1])
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.loc = newLoc
            elif self.lastMoveDir == 2:
                newLoc = (self.loc[0],max(self.loc[1]-1,0))
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.loc = newLoc
            else:
                newLoc = (max(self.loc[0]-1, 0),self.loc[1])
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.loc = newLoc
        # MY = move north/south (+/-)
        if self.actionOutputs[7] > self.PERFORM_ACTION:
            if self.actionOutputs[7] < self.PERFORM_ACTION+ (1-self.PERFORM_ACTION)/2: # south
                newY = self.loc[1]-1
                if newY < 0:
                    newY = 0
                newLoc = (self.loc[0],newY)
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.loc = newLoc
                    self.lastMoveDir = 1
            else:                           # north
                newY = self.loc[1]+1
                if newY >= grid.sizeY:
                    newY = grid.sizeY-1
                newLoc = (self.loc[0],newY)
                if not grid.isOccupied(newLoc[0],newLoc[1]):
                    grid.updateIndex(self.loc,newLoc,self.index)
                    self.loc = newLoc
                    self.lastMoveDir = 3
        
    # use nnet to generate actions, and perform them
    def feedForward(self, simStep, grid):
        self.genSensoryData(grid,simStep)
        self.sumInternalFromSensory()
        self.sumActionFromSensory()

        self.InternalTanH()

        self.sumInternalFromInternal()       
        self.sumActionFromInternal()

        self.ActionTanH()

        self.RunActions(grid)
    
