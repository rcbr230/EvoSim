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

MAX_GENERATIONS = 100
MAX_STEPS = 128
POP_SIZE = 1000
GRID_X = 128
GRID_Y = 128
peeps = Peeps(POP_SIZE)
grid = Grid(GRID_X,GRID_Y, peeps)
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
        canvas.delete("all")
        grid.DrawGrid(canvas)
        root.update()
        for index in range(1, POP_SIZE+1):
            if peeps.getIndividual(index).isAlive():
                simStepOneIndividual(peeps.getIndividual(index),i, index)

    # CREATE NEW GEN FROM PREV GEN

    newGen = peeps.cull(grid,SurvivalConditions.LeftandRight)
    print("SURVIVED: " + str(len(newGen)))
    newGenomes = []
    for i in range(0,POP_SIZE):
        parent1 = newGen[random.randint(0,len(newGen)-1)]
        parent2 = newGen[random.randint(0,len(newGen)-1)]
        newGenomes.append(peeps.getIndividual(parent1).genome.breedGenomes(peeps.getIndividual(parent2).genome))
    grid.ZeroBoard()
    peeps = Peeps(POP_SIZE)
    for i in range(1,POP_SIZE+1):
        loc = grid.FindEmptyLocation()
        peeps.initPeep(i,loc,newGenomes[i-1])

        grid.setIndex(loc,i)
    print("NEW GEN STARTING " + str(generation+1))
    generation += 1
root.mainloop()