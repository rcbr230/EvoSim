"""
This is the top level of the simulation that a user can interact with.

"""
from enum import Enum, auto
from Grid import Grid
from Peeps import Peeps
import tkinter as TK
import time

MAX_GENERATIONS = 1
MAX_STEPS = 100
POP_SIZE = 1000
GRID_X = 128
GRID_Y = 128
grid = Grid(GRID_X,GRID_Y)
peeps = Peeps(POP_SIZE)
generation = 0

class SurvivalConditions(Enum):
    LeftandRight = auto()
    Center = auto()
    Top = auto()
    Bottom = auto()
# refill pop to max size
def repopulate(survPop):
    for i in range(len(survPop),POP_SIZE):
        pass

# return an array of peep indexes that pass some condition
def cull(grid, condition):
    if condition == SurvivalConditions.LeftandRight:
        leftBounds = grid.sizeX/4
        rightBounds = grid.sizeX/4*3,grid.sizeX
        survivingPop = [0]
        highestIndex = 1
        for i in range(len(grid.sizeY)):
            for j in range(0,leftBounds):
                if grid.gridInfo[i][j] != 0:
                    survivingPop.append(grid.gridInfo[i][j])
        for i in range(len(grid.sizeY)):
            for j in range(rightBounds,grid.sizeX):
                if grid.gridInfo[i][j] != 0:
                    survivingPop.append(grid.gridInfo[i][j])
    return survivingPop           

def simStepOneIndividual(indiv, simStep, instance):
    indiv.age += 1
    indiv.feedForward(simStep,grid)

def CreateGen0():
    for i in range(1,POP_SIZE+1):
        loc = grid.FindEmptyLocation()
        peeps.initPeep(i,loc)
        # peeps.individuals[i].CreateWiring()
        grid.setIndex(loc,i)


root = TK.Tk()
canvas = TK.Canvas(root, width=128*5, height=128*5)
canvas.pack()

# init and place the first generation onto the grid!!!
CreateGen0()
grid.DrawGrid(canvas)


while generation < MAX_GENERATIONS:
    for i in range(MAX_STEPS):
        grid.DrawGrid(canvas)
        root.update()
        for index in range(1, POP_SIZE+1):
            if peeps.getIndividual(index).isAlive():
                simStepOneIndividual(peeps.getIndividual(index),i, index)
        print(str(i) + " ",end=" ")
    print("Generation " + generation)

    # CREATE NEW GEN FROM PREV GEN
    newGeneration = cull(grid, SurvivalConditions.LeftandRight)
    newGeneration = repopulate(newGeneration)
    generation += 1
root.mainloop()
