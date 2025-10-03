
This repository is intended to store the code needed for the CS 499 project at the University of Kentucky. 

How to run:
`py Simulator.py`

Good default values when prompted are:
30 - generations: How many times a new generation will be created
50 - steps: How many moves an indivudal can take in one generation
500 - population size NOTE: A high pop will cause a lot of collisions and possibly slow down the learning process.


How does it work?

Each dot has its own brain with a varying size of genes(2-10). The genes determine what parts of the dots brain connect and how they interact with eachother. 
__For example:__
Gene - 0 0101110 1 1000111 0110111000110101
       Starting Sensory/Internal | Which node | Connecting Internal/Action | Which node | weight
Lets say the gene above is: 
        Sensory | Nearest wall location | Action | Move towards wall | <weight>
This means that when this gene is used it will determine how far the nearest wall is, multiply that by the weight, and if it surpasses some condition it will perform the action.

Once the dots have all moved the max number of steps the program will kill anything not near the left and right walls of the environment. Then it will use the survivors to breed them and create a new generation and start the process again.


Hope that makes sense :P
