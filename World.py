import os
import pygame


class World:

    def __init__(self):
        self.objectImageMapping = []
        self.objects = []
        self.objectDef = []
        self.attributes = {}

    def loadWorldFromFile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                if line[0] == '#':
                    attr = World.parseAttributeFromString(line)
                    self.attributes[attr.name] = attr.value
                elif line[0] == '@':
                    self.objectDef.append(World.parseObjectDefFromString(line))
                else:
                    self.objects.append(World.parseObjectFromString(line))
        self.objectImageMapping = self.initImageMapping()

    @staticmethod
    def parseAttributeFromString(strLine):
        values = strLine[1:].split(';')
        return Attribute(values[0], values[1].rstrip())

    @staticmethod
    def parseObjectDefFromString(strLine):
        values = strLine[1:].split(';')
        return Definition(values[1], values[0], values[2])

    @staticmethod
    def parseObjectFromString(strLine):
        values = strLine.split(';')
        return Tile(values[0], int(values[1]), int(values[2]))

    def initImageMapping(self):
        mapping = {}
        for definition in self.objectDef:
            mapping[definition.name] = pygame.image.load('images/' + definition.imageName + '.png')
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