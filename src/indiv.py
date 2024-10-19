
import random
from Genome import Genome

"""
alive
age
genome
nnet - this is what uses the genome
reponsiveness
last move direction

"""
class indiv:
    
    def __init__(self, loc_:tuple):
        self.alive = True
        self.loc = loc_
        self.age = 0
        self.lastMoveDir = random.randint(0,3) # 0-up, 1-right, 2-down, 3-left
        g = Genome()
        g.makeRandomGenome()
        self.genome = g
        self.genome.createWiring()

    def isAlive(self):
        return self.alive
    
    # use nnet to generate actions, and perform them
    def runActions(self, simStep, grid, instance):


        # THIS IS JUST RANDOM MOVEMENT AND IS THERE AS AN EXAMPLE FOR HOW IT MAY LOOK IN THE FUTURE!!!!
        newLoc = [self.loc[0] + random.randint(-1,1), self.loc[1] + random.randint(-1,1)]
        if newLoc[0] < 0:
            newLoc[0] = 0
        if newLoc[0] >= grid.sizeX:
            newLoc[0] = grid.sizeX - 1
        if newLoc[1] < 0:
            newLoc[1] = 0
        if newLoc[1] >= grid.sizeY:
            newLoc[1] = grid.sizeY - 1
        grid.updateIndex(self.loc, newLoc, instance)
        self.loc = tuple(newLoc)