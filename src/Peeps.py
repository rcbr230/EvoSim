
from indiv import indiv
class Peeps:


    def __init__(self,population:int):
        self.individuals = [indiv] * population+1 # index 0 cannot be used, so add 1
    
    def getIndividual(self,index):
        return self.individuals[index]