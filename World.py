import os
import pygame


class World:

    def __init__(self):
        self.objectImageMapping = World.initImageMapping()
        self.objects = []

    def loadWorldFromFile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.objects.append(World.parseObjectFromString(line))

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


class Tile:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y