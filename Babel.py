from WorldGeneration import *
from World import *


class LibraryOfBabel (WorldGeneration):

    def __init__(self, seed):
        WorldGeneration.__init__(self, seed)

    def _generateWorld(self):
        world = World()
        for x in range(0, 21, 4):
            for y in range(0, 21, 4):
                unit = Unit("lob-room")
                for objDef in unit.objectDef:
                    if not world.objectDef.__contains__(objDef):
                        world.objectDef.append(objDef)
                for obj in unit.objects:
                    translatedObj = Tile(obj.name, obj.x + x, obj.y + y, obj.z)
                    world.objects.append(translatedObj)
        return world


class Unit(World):

    def __init__(self, name):
        World.__init__(self)
        self.loadWorldFromFile("units/" + name + ".pfe")