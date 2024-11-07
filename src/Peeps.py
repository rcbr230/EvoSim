
from SurvivalCond import SurvivalConditions
from indiv import indiv

class Peeps:
    def __init__(self,population:int):
        self.individuals = [None] * (population+1) # index 0 cannot be used, so add 1
        
    # def initPeep(self,index,loc):
    #     self.individuals[index] = indiv(loc,index)
    def initPeep(self,index,loc,genome=0):
        self.individuals[index] = indiv(loc,index,genome)
    def getIndividual(self,index):
        return self.individuals[index]
    
    # return an array of peep indexes that pass some condition
    def cull(self, grid, condition):
        if condition == SurvivalConditions.LeftandRight:
            leftBounds = int(grid.sizeX/4)
            rightBounds = int(grid.sizeX/4*3)
            survivingPop = []
            for i in range(grid.sizeY):
                for j in range(0,leftBounds):
                    if grid.gridInfo[i][j] != 0:
                        survivingPop.append(grid.gridInfo[i][j])
            for i in range(grid.sizeY):
                for j in range(rightBounds,grid.sizeX):
                    if grid.gridInfo[i][j] != 0:
                        survivingPop.append(grid.gridInfo[i][j])
        return survivingPop           
