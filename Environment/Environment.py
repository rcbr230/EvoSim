"""
Author: Reece Brogden
Purpose: This will contain the logic on how the entity will interact with the environment.
        NOTE: This does NOT determine how entities interact with eachother. It only determines what
            is avalible to the entities. (eg. food for herbivores). The goal is to just randomly place entities around
            the environment and let them interact.
        All environments will be the same size grid, 50x50. Entities are "outside" of the grid when not in a cycle.
Created: 10/17/2024
"""
import random
class BaseEnviroment:
    
    def __init__(self):
        self.Grid_ = [[0]*50]*50
        self.Scarity_ = 0.1
    