"""
    Sensory Inputs:
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
# full gene 01110001110110100001111111100011

import random
import time
# w = action effects the environment!




class Genome:
    SENSORY_NEURONS = 18
    INTERNAL_NEURONS = 3
    ACTION_NEURONS = 9  
    MIN_GENE_LENGTH = 2
    MAX_GENE_LENGTH = 10
    GenomeList = []

    def makeRandomGene(self):
        gene = Gene()
        gene.sourceType = random.randint(0,1)
        gene.sourceNum = random.randint(0,127) # 2^7-1
        gene.sinkType = random.randint(0,1)
        gene.sinkNum = random.randint(0,127) # 2^7 -1
        gene.weight = 1/random.randint(1,65535) # 2^16 -1
        # gene.weight = 1/random.randint(1,10000) # 2^16 -1

        return gene
    
    # flip a random bit in the genome
    def randomMutation(self):
        
        rGene = random.randint(0,len(self.GenomeList)-1)
        rPart = random.randint(0,4)
        if rPart == 0:
            self.GenomeList[rGene].sourceType = not self.GenomeList[rGene].sourceType
        elif rPart == 1:
            self.GenomeList[rGene].sourceNum = random.randint(0,127) # 2^7-1
        elif rPart == 2:
            self.GenomeList[rGene].sinkType = not self.GenomeList[rGene].sinkType
        elif rPart == 3:
            self.GenomeList[rGene].sinkNum = random.randint(0,127) # 2^7-1
        else:
            self.GenomeList[rGene].weight = 1/random.randint(1,65535) # 2^16 -1
            
    def makeRandomGenome(self):
        genome = Genome()
        # genomeLength = random.randint(self.MIN_GENE_LENGTH, self.MAX_GENE_LENGTH)
        genomeLength = 10
        for i in range(genomeLength):
            self.GenomeList.append(self.makeRandomGene())

    def returnAsString(self):
        genes = []
        for gene in self.GenomeList:
            src = '{0:01b}'.format(gene.sourceType)
            genes.append(src)
        return genes

    def breedGenomes(self, other):
        g = Genome()
        for i in range(len(self.GenomeList)):
            randGenome = random.randint(0,1)
            if randGenome == 0:
                g.GenomeList.append(self.GenomeList[i])
            else:
                g.GenomeList.append(other.GenomeList[i])
        return g
    
    #helper for getColor()
    @staticmethod
    def intToHexTwoDig(n):
        rv = ""
        sixteens = n // 16
        ones = n % 16
        #sixteens place
        match sixteens:
            case 10:
                rv += "a"
            case 11:
                rv += "b"
            case 12:
                rv += "c"
            case 13:
                rv += "d"
            case 14:
                rv += "e"
            case 15:
                rv += "f"
            case _: #0-9
                rv += str(sixteens)
        #ones place
        match ones:
            case 10:
                rv += "a"
            case 11:
                rv += "b"
            case 12:
                rv += "c"
            case 13:
                rv += "d"
            case 14:
                rv += "e"
            case 15:
                rv += "f"
            case _: #0-9
                rv += str(ones)
        return rv
    
    def getColor(self):
        totalSourceNum = 0
        totalSinkNum = 0
        totalWeight = 0.0
        for gene in self.GenomeList:
            totalSourceNum += gene.sourceNum
            totalSinkNum += gene.sinkNum
            totalWeight += gene.weight
        sz = len(self.GenomeList)
        avgSourceNum = totalSourceNum / sz
        avgSinkNum = totalSinkNum / sz
        avgWeight = totalWeight / sz
        r = avgSourceNum / 127 * 255
        g = avgSinkNum / 127 * 255
        b = avgWeight * 255
        rv = "#" + Genome.intToHexTwoDig(int(r)) + Genome.intToHexTwoDig(int(g)) + Genome.intToHexTwoDig(int(b))
        print("DEBUG: Color hex is " + rv)
        return rv

    

    def __init__(self):
        self.GenomeList = []
    

class Gene:

    def __init__(self):
        self.sourceType = 0
        self.sourceNum = 0
        self.sinkType = 0
        self.sinkNum = 0
        self.weight = 0
    
    def printHex(self):
        strFormat = format(self.sourceType, '01b') + format(self.sourceNum, '07b') +  format(self.sinkType, '01b') +  format(self.sinkNum, '07b') +  format(self.weight, '016b')
        # print(hex(int(strFormat)))
        print(strFormat)
