
"""
This is the top level of the simulation that a user can interact with.

"""
from Grid import Grid
from Peeps import Peeps

def simStepOneIndividual(indiv, simStep):
    pass


MAX_GENERATIONS = 10
MAX_STEPS = 30
POP_SIZE = 1000
GRID_X = 128
GRID_Y = 128
grid = Grid(GRID_X,GRID_Y)
peeps = Peeps(POP_SIZE)
generation = 0

while generation < MAX_GENERATIONS:

    for i in range(MAX_STEPS):
        for index in range(1, POP_SIZE):
            if peeps.getIndividual(index).isAlive():
                simStepOneIndividual(peeps.getIndividual(index),i)

    generation += 1

