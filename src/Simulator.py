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
MAX_STEPS = 1000
POP_SIZE = 10
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
        grid.DrawGrid(canvas)
        root.after(1,root.update())
        for index in range(1, POP_SIZE+1):
            if peeps.getIndividual(index).isAlive():
                simStepOneIndividual(peeps.getIndividual(index),i, index)

    # CREATE NEW GEN FROM PREV GEN
    newGen = peeps.cull(grid,SurvivalConditions.LeftandRight)
    newGenomes = []
    for i in range(0,POP_SIZE):
        parent1 = newGen[random.randint(0,len(newGen)-1)]
        parent2 = newGen[random.randint(0,len(newGen)-1)]
        t1 = time.time()
        newGenomes.append(peeps.getIndividual(parent1).genome.breedGenomes(peeps.getIndividual(parent2).genome))
        print(str(time.time() - t1))
    print("done1")
    grid.ZeroBoard()
    peeps = Peeps(POP_SIZE)
    for i in range(1,POP_SIZE+1):
        t1 = time.time()
        loc = grid.FindEmptyLocation()
        peeps.initPeep(i,loc,newGenomes[i-1])
        print(str(time.time() - t1))

        grid.setIndex(loc,i)
    print("NEW GEN STARTING " + str(generation+1))
    exit(0)
    generation += 1
