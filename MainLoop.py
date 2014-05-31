import pygame
from GameState import *

from pygame.locals import *

FRAMES_PER_SECOND = 30

pygame.init()

colorBlack = pygame.Color(0, 0, 0)
colorWhite = pygame.Color(255, 255, 255)

gameState = GameState()

screen = pygame.display.set_mode((1024, 758))
pygame.display.set_caption('Procedural Generation Viewer')
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)

gameState.advanceCurrentState()
while gameState.getCurrentState() == gameState.GAME_STATE_RUNNING:
    levelName = font.render('Testlevel', False, colorWhite)
    rectangle = levelName.get_rect()
    screen.blit(levelName, rectangle)

    for event in pygame.event.get():
        if event.type == QUIT:
            gameState.advanceCurrentState()

    pygame.display.update()
    deltaTime = clock.tick(FRAMES_PER_SECOND)

pygame.quit()
