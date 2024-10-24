# Grid.py

import random 
import tkinter as TK
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
                return (x,y)
            
    # Check if a space is occupied. If it is then output true and the entity's index
    def isOccupied(self,x,y):
        if self.gridInfo[x][y] != 0:
            return True,self.gridInfo[x][y]
        return False
    
    def setIndex(self,loc,i):
        self.gridInfo[loc[0]][loc[1]] = i

    def updateIndex(self, prevLoc, newLoc, i):
        self.gridInfo[prevLoc[0]][prevLoc[1]] = 0
        self.gridInfo[newLoc[0]][newLoc[1]] = i

    def ZeroBoard(self):
        self.gridInfo = [[0 for i in range(self.sizeX)] for i in range(self.sizeY)]
        
    def DrawGrid(self,canvas):
        clrs = ["black","blue","red","yellow","green"]
        canvas.create_rectangle(0,0,1000,1000,fill="white")
        for i in range(len(self.gridInfo)):
            for j in range(len(self.gridInfo)):
                if self.gridInfo[i][j] != 0:
                    canvas.create_oval(i*5,j*5,i*5+5,j*5+5,fill=clrs[self.gridInfo[i][j] % 5])
    # ADD IN "SURVIVAL CONDITIONS"
    # Cull peeps in a certain area
        # Rect
        # Oval
        # Corners
        # N/S sides
        # E/W sides

        # PLEASE PROVIDE CONSTRAINTS TO THESE FUNCTIONS

    


