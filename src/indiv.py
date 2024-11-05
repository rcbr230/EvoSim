
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
    

    def GenSensoryInputs(self, simStep, grid):
        SENSORY_NODES = 18
        ret = [-1]*18
        for i in range(len(self.NeuronList)):
            if i % 3 != 0 and self.NeuronList[i][1] != NodeVal.Sensory:
                continue
            
            # check what sensory nodes
            #AGE
            if self.NeuronList[i]   == 0:
                ret[0] = simStep
            #RND
            elif self.NeuronList[i] == 1:
                ret[1] = random.randint(0,1000)
            #BLR blockage left-right
            elif self.NeuronList[i] == 2:
                ret[2] = grid.gridInfo[self.loc[0]+1] + grid.gridInfo[self.loc[0]-1]
                if(ret != 0):
                    ret[2] = 1
            #OSC
            elif self.NeuronList[i] == 3:
                ret[3] = int(self.curOsc)
                self.curOsc = not self.curOsc
            #BFD 
            elif self.NeuronList[i] == 4:
                #up
                if self.lastMoveDir == 0:
                    ret[4] = grid.gridInfo[self.loc[1]+1]
                    if(ret != 0):
                        ret[4] = 1
                #down
                elif self.lastMoveDir == 0:
                    ret[4] = grid.gridInfo[self.loc[1]-1]
                    if(ret != 0):
                        ret[4] = 1
                #right
                elif self.lastMoveDir == 0:
                    ret[4] = grid.gridInfo[self.loc[0]+1]
                    if(ret != 0):
                        ret[4] = 1
                #left
                elif self.lastMoveDir == 0:
                    ret[4] = grid.gridInfo[self.loc[0]-1]
                    if(ret != 0):
                        ret[4] = 1
            #Plr - pop  gradiant right
            elif self.NeuronList[i] == 5:
                # implement later--------------------------------------------------------
                pass
            #Pop - pop density
            elif self.NeuronList[i] == 6:
                # implement later--------------------------------------------------------
                pass
            #Pfd - pop gradient forward
            elif self.NeuronList[i] == 7:
                # implement later--------------------------------------------------------
                pass
            #LPf - pop long-range forward
            elif self.NeuronList[i] == 8:
                # implement later--------------------------------------------------------
                pass
            #LMy - last movement y
            elif self.NeuronList[i] == 9:
                # implement later--------------------------------------------------------
                pass
            #LBf - long-range block foward
            elif self.NeuronList[i] == 10:
                # implement later--------------------------------------------------------
                pass
            #LMx - last movement x
            elif self.NeuronList[i] == 11:
                # implement later--------------------------------------------------------
                pass
            #BDy - boarder distance y
            elif self.NeuronList[i] == 12:
                ret[12] = min(self.loc[1], len(grid.gridinfo[0])-self.loc[1])
            #Gen - genetic similarity to forward indiv
            elif self.NeuronList[i] == 13:
                # implement later--------------------------------------------------------
                pass
            #BDx - boarder distance x
            elif self.NeuronList[i] == 14:
                ret[14] = min(self.loc[0], len(grid.gridinfo[0])-self.loc[0])
            #Lx - x location
            elif self.NeuronList[i] == 15:
                ret[15] = self.loc[0]
            #BD - nearest boarder dist
            elif self.NeuronList[i] == 16:
                ret[16] = min(min(self.loc[0], len(grid.gridinfo[0])-self.loc[0]),min(self.loc[1], len(grid.gridinfo[0])-self.loc[1]))
            #Ly -  y loc
            elif self.NeuronList[i] == 17:
                ret[17] = self.loc[1]
            
    def FindNeurons(self):
        TOTAL_SENSORY  = 18
        TOTAL_INTERNAL = 6
        TOTAL_ACTION   = 9

        # APPENDED SO THAT: (src,nodeVal), weight, (src,nodeVal)
        ret = []
        for i in self.genome.GenomeList:
            # FIRST NODE:
            # 0 = sensory
            if i.source == 0:
                node = i.sourceNum % TOTAL_SENSORY
                val = NodeVal.Sensory
                ret.append((node,val))
            # it's 1, 1 = internal
            else:
                node = i.sourceNum % TOTAL_INTERNAL
                val = NodeVal.Internal
                ret.append((node,val))
                ret.append(node)
            
            ret.append(i.weight)

            # SECOND NODE:
            # 0 = internal
            if i.sink == 0:
                node = i.sinkNum % TOTAL_INTERNAL
                val = NodeVal.Internal
                ret.append((node,val))
            # it's 1, 1 = action
            else:
                node = i.sinkNum % TOTAL_ACTION
                val = NodeVal.Action
                ret.append((node,val))

        return ret
            
    def determineAction(self, startIndex):
        pass

    def CreateWiring(self):
        self.NeuronList = self.FindNeurons()
        

    def RandMutation(self):
        pass
        #implement later.

class NodeVal(Enum):
    Sensory  = 0
    Internal = 1
    Action   = 2
