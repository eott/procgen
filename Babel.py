from WorldGeneration import *
from World import *


class LibraryOfBabel (WorldGeneration):

    def __init__(self, seed):
        WorldGeneration.__init__(self, seed)

    def _generateWorld(self):
        unit = Unit("lob-room")
        return unit


class Unit(World):

    def __init__(self, name):
        World.__init__(self)
        self.loadWorldFromFile("units/" + name + ".pfe")