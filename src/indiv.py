
import random
from Genome import Genome
class indiv:
    
    def __init__(self, index_:int,loc_:tuple, genome:Genome):
        self.alive = True
        self.index = index_
        self.loc = loc_
        self.age = 0
        self.lastMoveDir = random.randint(0,3) # 0-up, 1-right, 2-down, 3-left

