import os
import pygame


class World:
    """Represents the game world and provides access to the game objects within it. The world file should be in the
    following format:

    * Each line contains either a world attribute, an object definition or an instance of an object.
    * The order does not matter, but readability is encouraged
    * The fields of each line are separated by a semicolon and must be in the correct order
    * A line starting (logically ending) with a new line or carriage return character is ignored
    * A world attribute starts with # and has the fields:
            0 : Attribute name
            1 : Value
    * An object definition starts with @ and has the fields:
            0 : Image filename, without extension (images are assumed to be in .png format
            1 : Object name (identifier)
            2 : Human readable description and other information
    * An object instance starts with any character but @ and # and has the fields:
            0 : Object name
            1 : x coordinate, in units of tile size
            2 : y coordinate, in units of tile size
    """

    def __init__(self):
        self.objectImageMapping = []
        self.objects = []
        self.objectDef = []
        self.attributes = {}

    def loadWorldFromFile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                if line[0] == "\n" or line[0] == "\r":
                    continue
                elif line[0] == '#':
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