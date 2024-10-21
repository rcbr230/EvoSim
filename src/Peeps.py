
from indiv import indiv
class Peeps:


    def __init__(self,population:int):
        self.individuals = [None] * (population+1) # index 0 cannot be used, so add 1
        
    def initPeep(self,index,loc):
        self.individuals[index] = indiv(loc,index)

    def getIndividual(self,index):
        return self.individuals[index]