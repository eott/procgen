class World:

    objectImageMapping = {}
    objects = []

    def loadWorldFromFile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.objects.append(World.parseObjectFromString(line))

    @staticmethod
    def parseObjectFromString(strLine):
        values = strLine.split(';')
        return Tile(values[0], values[1], values[2])


class Tile:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y