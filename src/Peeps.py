
from SurvivalCond import SurvivalConditions
from indiv import indiv

class Peeps:
    def __init__(self,population:int):
        self.individuals = [None for _ in range(population+1)] # index 0 cannot be used, so add 1
        
    # def initPeep(self,index,loc):
    #     self.individuals[index] = indiv(loc,index)
    def initPeep(self,index,loc,genome=0):
        self.individuals[index] = indiv(loc,index,genome)

    def getIndividual(self,index):
        return self.individuals[index]
    
    # return an array of peep indexes that pass some condition
    def cull(self, grid, condition):
        survivingPop = []
        dist = 8
        leftBounds = int(grid.sizeX/dist)
        rightBounds = int(grid.sizeX/dist*(dist-1))
        topBounds = int(grid.sizeY/dist)
        bottomBounds = int(grid.sizeY/dist*(dist-1))
        if condition == SurvivalConditions.LeftandRight:
            for i in range(grid.sizeY):
                for j in range(0,leftBounds):
                    if grid.gridInfo[j][i] != 0:
                        survivingPop.append(grid.gridInfo[j][i])
            for i in range(grid.sizeY):
                for j in range(rightBounds,grid.sizeX):
                    if grid.gridInfo[j][i] != 0:
                        survivingPop.append(grid.gridInfo[j][i])
        if condition == SurvivalConditions.Left:
            for i in range(grid.sizeY):
                for j in range(0,leftBounds):
                    if grid.gridInfo[j][i] != 0:
                        survivingPop.append(grid.gridInfo[j][i])
        if condition == SurvivalConditions.Right:
            for i in range(grid.sizeY):
                for j in range(rightBounds,grid.sizeX):
                    if grid.gridInfo[j][i] != 0:
                        survivingPop.append(grid.gridInfo[j][i])
        centerTopBound = int(grid.sizeY/3)
        centerBotBound = centerTopBound*2
        centerLeftBound = int(grid.sizeX/3)
        cetnerRightBound = centerLeftBound*3
        if condition == SurvivalConditions.Center:
            for i in range(centerTopBound, centerBotBound):
                for j in range(centerLeftBound, cetnerRightBound):
                    if grid.gridInfo[j][i] != 0:
                        survivingPop.append(grid.gridInfo[j][i])
        if condition == SurvivalConditions.Top:
            for i in range(0, topBounds):
                for j in range(grid.sizeX):
                    if grid.gridInfo[j][i] != 0:
                        survivingPop.append(grid.gridInfo[j][i])
        if condition == SurvivalConditions.Bottom:
            for i in range(bottomBounds, grid.sizeY):
                for j in range(grid.sizeX):
                    if grid.gridInfo[j][i] != 0:
                        survivingPop.append(grid.gridInfo[j][i])
        if condition == SurvivalConditions.TopandBottom:
            for i in range(0, topBounds):
                for j in range(grid.sizeX):
                    if grid.gridInfo[j][i] != 0:
                        survivingPop.append(grid.gridInfo[j][i])
            for i in range(bottomBounds, grid.sizeY):
                for j in range(grid.sizeX):
                    if grid.gridInfo[j][i] != 0:
                        survivingPop.append(grid.gridInfo[j][i])
        
        return survivingPop           
