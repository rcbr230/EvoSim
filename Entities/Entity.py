"""
Author: Reece Brogden
Purpose: Default is a base entity, but there are also 
Created: 10/17/2024
"""

class Entity:


    # create a living entity, hp default is 10, exists, and create a dict of attributes
    def __init__(self, reproducing:str):
        self.Attributes_ = {} # dict of attributes that can be used to determine interactions.

    # add an attribute to the dict
    def AddAttribute(self,key,item):
        self.Attributes_[key] = item
    
    # return an attribute 
    def GetAttribute(self,key):
        return self.Attributes_[key]
    
    def RemoveAttribute(self,key):
        del self.Attributes_[key]
