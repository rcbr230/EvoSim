# Grid.py

import random 
"""
Grid holds all the data of what is where. It knows EMPTY, BARRIER, or some index for an entity

"""
class Grid:

    EMPTY = 0
    BARRIER = 0xffff
    
    # create a grid of size x,y all filled with zeros
    def __init__(self,x,y):
        self.sizeX = x
        self.sizeY = y
        self.gridInfo = [[0 for i in range(self.sizeX)] for i in range(self.sizeY)]

    # find an empty location on the grid. No barriers or other individuals.
    def FindEmptyLocation(self):

        while True:
            x = random.randint(0,self.sizeX-1)
            y = random.randint(0,self.sizeY-1)
            if self.gridInfo[x][y] == 0:
                return x,y
            
    # Check if a space is occupied. If it is then output true and the entity's index
    def isOccupied(self,x,y):
        if self.gridInfo[x][y] != 0:
            return True,self.gridInfo[x][y]
        return False
    


