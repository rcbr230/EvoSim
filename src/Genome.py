"""
    Sensory Inputs:
    Slr = pheromone gradient left-right
    Sfd = pheromone gradient forward
    Sg = pheromone density
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

    Action Outputs:
    LPD = set long-probe distance
    Kill = kill forward neighbor.      Prob leave disabled
    OSC = set oscillator period
    SG = emit pheromone
    Res = set responsiveness
    Mfd = move forward
    Mrn = move random
    Mrv = move reverse
    MRL = move left/right (+/-)
    MX = move east/west (+/-)
    MY = move north/south (+/-)


    IGNORE PHERAMONES FOR NOW
    """
# GENE EX:             0                                           1110001                                    1   
#        Source(sensory or internal node)    Which neuron is it coming from(this num % num of neurons)   Sink type(where is the connection pointing to(action or internal)) CONT,
#           011010                                                              0001111111100011
#          Which neuron is it going to(this num % num of neurons          Weight. Divide this number by 10000.
import random

class Genome:
    SENSORY_NEURONS = 18
    INTERNAL_NEURONS = 3
    ACTION_NEURONS = 9  
    def makeRandomGene(self):
        gene = Gene()
        gene.source = bool(random.randint(0,1))
        gene.sourceNum = random.randint(0,255) 
        gene.sinkType = bool(random.randint(0,1))
        gene.sinkNum = random.randint(0,255)
        gene.weight = 0
    def createWiring(self):
        pass

class Gene:

    def __init__(self):
        self.source = 0
        self.sourceNum = 0
        self.sinkType = 0
        self.sinkNum = 0
        self.weight = 0