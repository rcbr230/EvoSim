
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
            if i % 3 != 0:
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
                pass
            elif self.NeuronList[i] == 6:
                pass
            elif self.NeuronList[i] == 7:
                pass
            elif self.NeuronList[i] == 8:
                pass
            elif self.NeuronList[i] == 9:
                pass
            elif self.NeuronList[i] == 10:
                pass
            elif self.NeuronList[i] == 11:
                pass
            elif self.NeuronList[i] == 12:
                pass
            elif self.NeuronList[i] == 13:
                pass
            elif self.NeuronList[i] == 14:
                pass
            elif self.NeuronList[i] == 15:
                pass
            elif self.NeuronList[i] == 16:
                pass
            elif self.NeuronList[i] == 17:
                pass
            
    def FindNeurons(self):
        TOTAL_SENSORY  = 18
        TOTAL_INTERNAL = 6
        TOTAL_ACTION   = 9

        # APPENDED SO THAT: src, weight, dest
        ret = []
        for i in self.genome.GenomeList:
            # FIRST NODE:
            # 0 = sensory
            if i.source == 0:
                node = i.sourceNum % TOTAL_SENSORY
                ret.append(node)
            # it's 1, 1 = internal
            else:
                node = i.sourceNum % TOTAL_INTERNAL
                ret.append(node)
            
            ret.append(i.weight)

            # SECOND NODE:
            # 0 = internal
            if i.source == 0:
                node = i.sinkType % TOTAL_INTERNAL
                ret.append(node)
            # it's 1, 1 = action
            else:
                node = i.sinkNum % TOTAL_ACTION
                ret.append(node)

        return ret
            


    def CreateWiring(self):
        self.NeuronList = self.FindNeurons()
        

    def RandMutation(self):
        pass
        #implement later.