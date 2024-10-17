"""
Author: Reece Brogden
Purpose: Default is a base entity, but there are also 
Created: 10/17/2024
"""

class Entity:


    # create a living entity, hp default is 10, exists, and create a dict of attributes
    def __init__(self, reproducing:str):
        self.Exists_ = True
        self.Health_ = 10
        self.Attributes_ = {} # dict of attributes that can be used to determine interactions.
        
    # instant kill entity
    def KillEntity(self):
        self.Health_ = 0
        self.Exists_ = False
    
    # remove x hp from entity
    def Damage(self, dmg):
        self.Health_ -= dmg
    
    # perform interaction with other entities that are nearby. This will be run by the enviormnet
    def Interaction(self, otherEntity):
        pass

    # add an attribute to the dict
    def AddAttribute(self,key,item):
        self.Attributes_[key] = item
    
    # return an attribute 
    def GetAttribute(self,key):
        return self.Attributes_[key]
    
    def RemoveAttribute(self,key):
        del self.Attributes_[key]
