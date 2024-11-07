"""
This is the top level of the simulation that a user can interact with.

"""
import copy
from enum import Enum, auto
import random
from Grid import Grid
from Peeps import Peeps
import tkinter as TK
import time

from SurvivalCond import SurvivalConditions

MAX_GENERATIONS = 10
MAX_STEPS = 2
POP_SIZE = 1000
GRID_X = 128
GRID_Y = 128
grid = Grid(GRID_X,GRID_Y)
peeps = Peeps(POP_SIZE)
generation = 0


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

    # CREATE NEW GEN FROM PREV GEN
    newGeneration = peeps.cull(grid, SurvivalConditions.LeftandRight)
    grid.ZeroBoard()
    prevPop = copy.deepcopy(peeps)
    peeps = Peeps(POP_SIZE)
    for i in range(1,POP_SIZE+1):
        loc = grid.FindEmptyLocation()
        p1 = newGeneration[random.randint(0,len(newGeneration))]
        p2 = newGeneration[random.randint(0,len(newGeneration))]
    
        newGenome = prevPop.getIndividual(p1).genome.breedGenomes(prevPop.getIndividual(p2).genome)
        peeps.initPeep(i,loc,newGenome)
        # peeps.individuals[i].CreateWiring()
        grid.setIndex(loc,i)
    
    generation += 1
root.mainloop()
