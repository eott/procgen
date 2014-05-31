import pygame
from pygame.locals import *

FRAMES_PER_SECOND = 30

pygame.init()

colorBlack = pygame.Color(0, 0, 0)
colorWhite = pygame.Color(255, 255, 255)

screen = pygame.display.set_mode((1024, 758))
pygame.display.set_caption('Procedural Generation Viewer')
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)

keepRunning = True
while keepRunning:
    levelName = font.render('Testlevel', False, colorWhite)
    rectangle = levelName.get_rect()
    screen.blit(levelName, rectangle)

    for event in pygame.event.get():
        if event.type == QUIT:
            keepRunning = False

    pygame.display.update()
    deltaTime = clock.tick(FRAMES_PER_SECOND)

pygame.quit()
