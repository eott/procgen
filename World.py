class World:

    objectImageMapping = {}
    objects = []

    def loadWorldFromFile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.objects.append(World.parseObjectFromString(line))

    @staticmethod
    def parseObjectFromString(strLine):
        pass