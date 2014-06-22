from random import *


class WorldGeneration:

    def __init__(self, seed):
        self.seed = seed
        self.rand = Random()
        self.rand.seed(seed)

    def generateWorldFile(self, filepath, worldname):
        with open(filepath, 'w') as file:
            # World attributes
            file.write('#world_name;'+worldname+'\n')
            file.write('#seed;'+self.seed+'\n')

            # World data
            generatedWorld = self._generateWorld()
            for definition in generatedWorld.objectDef:
                file.write("@" + definition.imageName + ';' + definition.fileExtension + ';' + definition.name
                           + definition.description + "\n")
            for object in generatedWorld.objects:
                file.write(object.name + ';' + str(object.x) + ';' + str(object.y) + ';' + str(object.z) + "\n")