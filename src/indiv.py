
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

        # compute actions using genome here!
        self.GenSensoryInputs(simStep,grid)
        self.calcInternal()
        self.calcAction()
        self.runActions(grid)
        pass
    

    def GenSensoryInputs(self, simStep, grid):
        for i in range(2,len(self.NeuronList),3):
            if self.NeuronList[i][1] != NodeVal.Sensory:
                continue
            
            # check what sensory nodes
            #AGE
            if self.NeuronList[i][0]   == 0:
                self.NeuronList[i][2] = simStep
            #RND
            elif self.NeuronList[i] == 1:
                self.NeuronList[i][2] = random.randint(0,1000)
            #BLR blockage left-right
            elif self.NeuronList[i][0] == 2:
                self.NeuronList[i][2] = grid.gridInfo[self.loc[0]+1] + grid.gridInfo[self.loc[0]-1]
                if(self.NeuronList[i][2] != 0):
                    self.NeuronList[i][2] = 1
            #OSC
            elif self.NeuronList[i][0] == 3:
                self.NeuronList[i][2] = int(self.curOsc)
                self.curOsc = not self.curOsc
            #BFD 
            elif self.NeuronList[i][0] == 4:
                #up
                if self.lastMoveDir == 0:
                    self.NeuronList[i][2] = grid.gridInfo[self.loc[1]+1]
                    if(self.NeuronList[i][2] != 0):
                        self.NeuronList[i][2] = 1
                #down
                elif self.lastMoveDir == 0:
                    self.NeuronList[i][2] = grid.gridInfo[self.loc[1]-1]
                    if(self.NeuronList[i][2] != 0):
                        self.NeuronList[i][2] = 1
                #right
                elif self.lastMoveDir == 0:
                    self.NeuronList[i][2] = grid.gridInfo[self.loc[0]+1]
                    if(self.NeuronList[i][2] != 0):
                        self.NeuronList[i][2] = 1
                #left
                elif self.lastMoveDir == 0:
                    self.NeuronList[i][2] = grid.gridInfo[self.loc[0]-1]
                    if(self.NeuronList[i][2] != 0):
                        self.NeuronList[i][2] = 1
            #Plr - pop  gradiant right
            elif self.NeuronList[i][0] == 5:
                # implement later--------------------------------------------------------
                pass
            #Pop - pop density
            elif self.NeuronList[i][0] == 6:
                # implement later--------------------------------------------------------
                pass
            #Pfd - pop gradient forward
            elif self.NeuronList[i][0] == 7:
                # implement later--------------------------------------------------------
                pass
            #LPf - pop long-range forward
            elif self.NeuronList[i][0] == 8:
                # implement later--------------------------------------------------------
                pass
            #LMy - last movement y
            elif self.NeuronList[i][0] == 9:
                # implement later--------------------------------------------------------
                pass
            #LBf - long-range block foward
            elif self.NeuronList[i][0] == 10:
                # implement later--------------------------------------------------------
                pass
            #LMx - last movement x
            elif self.NeuronList[i][0] == 11:
                # implement later--------------------------------------------------------
                pass
            #BDy - boarder distance y
            elif self.NeuronList[i][0] == 12:
                self.NeuronList[i][2] = min(self.loc[1], len(grid.gridinfo[0])-self.loc[1])
            #Gen - genetic similarity to forward indiv
            elif self.NeuronList[i][0] == 13:
                # implement later--------------------------------------------------------
                pass
            #BDx - boarder distance x
            elif self.NeuronList[i][0] == 14:
                self.NeuronList[i][2] = min(self.loc[0], len(grid.gridinfo[0])-self.loc[0])
            #Lx - x location
            elif self.NeuronList[i] == 15:
                self.NeuronList[i][2] = self.loc[0]
            #BD - nearest boarder dist
            elif self.NeuronList[i][0] == 16:
                self.NeuronList[i][2] = min(min(self.loc[0], len(grid.gridinfo[0])-self.loc[0]),min(self.loc[1], len(grid.gridinfo[0])-self.loc[1]))
            #Ly -  y loc
            elif self.NeuronList[i][0] == 17:
                self.NeuronList[i][2] = self.loc[1]
            
    def CreateWiring(self):
        TOTAL_SENSORY  = 18
        TOTAL_INTERNAL = 6
        TOTAL_ACTION   = 6
        #
        self.sensorNeurons = [[] for _ in range(TOTAL_SENSORY)]
        self.internalNeurons = [[] for _ in range(TOTAL_SENSORY)]
        self.actionNeurons = [[] for _ in range(TOTAL_SENSORY)]
        for i in self.genome.GenomeList:
            # Sensory Neuron
            if i.source == 0:
                pass
            # Internal Neuron
            if i.source == 1 or i.sink == 0:
                pass
            # Action Neuron
            if i.sink == 1:
                pass
        
    """
    Update val in internal node
    """    
    def calcInternal(self):
        pass

    def calcAction(self):
        pass
    
    def runActions(self,grid):
        for i in range(2,len(self.NeuronList),3):
            if self.NeuronList[i][1] != NodeVal.Action:
                continue
            
            # Mfd = move forward
            if self.NeuronList[i][0] == 0 and self.NeuronList[i][2] > 0.5:
                self.moveForward(grid)
            # Mrn = move random
            if self.NeuronList[i][0] == 1 and self.NeuronList[i][2] > 0.5:
                self.moveRandom(grid)
            # Mrv = move reverse
            if self.NeuronList[i][0] == 2 and self.NeuronList[i][2] > 0.5:
                self.moveReverse(grid)
            # MRL = move left/right (+/-) (relative to forward)
            if self.NeuronList[i][0] == 3 and self.NeuronList[i][2] > 0.5:
                self.moveLR(grid)
            # MX = move east/west (+/-)
            if self.NeuronList[i][0] == 4 and self.NeuronList[i][2] > 0.5:
                self.moveEW(grid)
            # MY = move north/south (+/-)
            if self.NeuronList[i][0] == 5 and self.NeuronList[i][2] > 0.5:
                self.moveNS(grid)

                # TBD?
                # LPD = set long-probe distance
                # OSC = set oscillator period
                # Res = set responsiveness


    def RandMutation(self):
        pass
        #implement later.
    
    def moveForward(self,grid):
        pass

    def moveRandom(self,grid):
        ForwardBack = random.randint(-1,1)
        LeftRight = random.randint(-1,1)
        newX = min(grid.sizeX-1,self.loc[0]+ForwardBack)
        newY = min(grid.sizeY-1,self.loc[1]+LeftRight)
        newLoc = (newX,newY)
        grid.updateIndex(self.loc,newLoc,self.index)
        self.loc = newLoc

    def moveReverse(self,grid):
        pass
    def moveLR(self,grid):
        pass
    def moveEW(self,grid):
        pass
    def moveNS(self,grid):
        pass