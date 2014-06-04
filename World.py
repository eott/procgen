import os
import pygame


class World:

    def __init__(self):
        self.objectImageMapping = World.initImageMapping()
        self.objects = []
        self.objectDef = []
        self.attributes = []

    def loadWorldFromFile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                if line[0] == '#':
                    self.attributes.append(World.parseAttributeFromString(line))
                elif line[0] == '@':
                    self.objectDef.append(World.parseObjectDefFromString(line))
                else:
                    self.objects.append(World.parseObjectFromString(line))

    @staticmethod
    def parseAttributeFromString(strLine):
        values = strLine[1:].split(';')
        return Attribute(values[0], values[1])

    @staticmethod
    def parseObjectDefFromString(strLine):
        values = strLine[1:].split(';')
        return Definition(values[1], values[0], values[2])

    @staticmethod
    def parseObjectFromString(strLine):
        values = strLine.split(';')
        return Tile(values[0], int(values[1]), int(values[2]))

    @staticmethod
    def initImageMapping():
        mapping = {}
        for filename in os.listdir(os.getcwd()+'/images/'):
            mapping[filename.split('.', 1)[0]] = pygame.image.load('images/'+filename)
        return mapping


class Attribute:

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Definition:

    def __init__(self, name, imageName, description):
        self.name = name
        self.imageName = imageName
        self.description = description

class Tile:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y