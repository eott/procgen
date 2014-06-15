from random import *


class WorldGeneration:

    def __init__(self, seed):
        self.seed = seed
        self.rand = Random()
        self.rand.seed(seed)

    def generateWorldFile(self, filepath, worldname, width, height):
        with open(filepath, 'w') as file:
            # World attributes
            file.write('#world_name;'+worldname+'\n')
            file.write('#seed;'+self.seed+'\n')