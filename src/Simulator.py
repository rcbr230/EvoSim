"""
This is the top level of the simulation that a user can interact with.

"""
import csv
from enum import Enum, auto
import random
from Grid import Grid
from Peeps import Peeps
import tkinter as TK

from SurvivalCond import SurvivalConditions

MAX_GENERATIONS = 100
MAX_STEPS = 100
POP_SIZE = 1000
GRID_X = 128
GRID_Y = 128
peeps = Peeps(POP_SIZE)
grid = Grid(GRID_X,GRID_Y, peeps)
generation = 1

# data recording
GenerationalData = []
# format: GenNum, StartingPop, Survivors, Array of all genomes
GenomeData = []


def simStepOneIndividual(indiv, simStep, instance):
    indiv.age += 1
    indiv.feedForward(simStep,grid)

def CreateGen0():
    for i in range(1,POP_SIZE+1):
        loc = grid.FindEmptyLocation()
        peeps.initPeep(i,loc)
        # peeps.individuals[i].CreateWiring()
        grid.setIndex(loc,i)

def getGenomes():
    ret = []
    for i in range(1,POP_SIZE+1):
        ret.append(peeps.getIndividual(i).genome)
    return ret


root = TK.Tk()
canvas = TK.Canvas(root, width=128*5, height=128*5)
canvas.pack()

# init and place the first generation onto the grid!!!  
CreateGen0()
grid.DrawGrid(canvas)


while generation < MAX_GENERATIONS+1:
    print("NEW GEN STARTING " + str(generation))

    for i in range(MAX_STEPS):
        canvas.delete("all")
        grid.DrawGrid(canvas)
        root.update()
        for index in range(1, POP_SIZE+1):
            if peeps.getIndividual(index).isAlive():
                simStepOneIndividual(peeps.getIndividual(index),i, index)
    
    # CREATE NEW GEN FROM PREV GEN
    newGen = peeps.cull(grid,SurvivalConditions.LeftandRight)
    # record data from current population
    GenerationalData.append((generation,POP_SIZE,len(newGen)))
    GenomeData.append(getGenomes())

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
    count = 0
    for i in range(grid.sizeX):
        for j in range(grid.sizeY):
            if grid.gridInfo[i][j] != 0:
                count += 1
    print(f"POP SIZE: {count}")
    generation += 1


# Output all the recorded data.
with open('Gendata.csv','w') as f:
    writer = csv.writer(f)
    for row in GenerationalData:
        writer.writerow(row)
with open('GenomeData.csv','w') as f:
    writer = csv.writer(f)
    for i in range(MAX_GENERATIONS):
        for genome in GenomeData[i]:
            for gene in genome.GenomeList:
                geneStr = ''
                geneStr = str(gene.sourceType)+' '
                geneStr += str(gene.sourceNum)+' '
                geneStr += str(gene.sinkType)+' '
                geneStr += str(gene.sinkNum)+' '
                geneStr += str(gene.weight)+' '
                writer.writerow([str(i)]+[geneStr])
exit(0)