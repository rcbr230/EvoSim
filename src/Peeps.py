
from indiv import indiv
class Peeps:

    """
    Sensory Inputs:
    Slr = pheromone gradient left-right
    Sfd = pheromone gradient forward
    Sg = pheromone density
    Age = age
    Rnd = random input
    Blr = blockage left-right
    Osc = oscillator
    Bfd = blockage forward
    Plr = population gradient left-right
    Pop = population density
    Pfd = population gradient forward
    LPf = population long-range forward
    LMy = last movement Y
    LBf = blockage long-range forward
    LMx = last movement X
    BDy = north/south border distance
    Gen = genetic similarity of forward neighbor
    BDx = east/west border distance
    Lx = east/west world location
    BD = nearest border distance
    Ly = north/south world location

    Action Outputs:
    LPD = set long-probe distance
    Kill = kill forward neighbor.      Prob leave disabled
    OSC = set oscillator period
    SG = emit pheromone
    Res = set responsiveness
    Mfd = move forward
    Mrn = move random
    Mrv = move reverse
    MRL = move left/right (+/-)
    MX = move east/west (+/-)
    MY = move north/south (+/-)


    IGNORE PHERAMONES FOR NOW
    """

    def __init__(self,population:int):
        self.individuals = [indiv] * population+1 # index 0 cannot be used, so add 1