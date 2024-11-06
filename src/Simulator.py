"""
This is the top level of the simulation that a user can interact with.

"""
from Grid import Grid
from Peeps import Peeps
import tkinter as TK
import time

MAX_GENERATIONS = 1
MAX_STEPS = 100
POP_SIZE = 20
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
        peeps.individuals[i].CreateWiring()
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
        time.sleep(0.5)
        for index in range(1, POP_SIZE+1):
            if peeps.getIndividual(index).isAlive():
                simStepOneIndividual(peeps.getIndividual(index),i, index)
       
    # CREATE NEW GEN FROM PREV GEN

    generation += 1
root.mainloop()

