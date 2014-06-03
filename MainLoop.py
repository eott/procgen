import pygame
from GameState import *
from KeyMapping import *
from EventSystem import *
from GameEvent import *
from World import *
from Camera import *

from pygame.locals import *

# Useful constants
FRAMES_PER_SECOND = 30
TILESIZE = 32

# pygame's init method must be called before all other pygame methods
pygame.init()

# Define colors
colorBlack = pygame.Color(0, 0, 0)
colorWhite = pygame.Color(255, 255, 255)

# Define fonts
font = pygame.font.Font('freesansbold.ttf', 32)

# Init subsystems
eventSystem = EventSystem()
gameState = GameState()
clock = pygame.time.Clock()
world = World()
world.loadWorldFromFile('Testworld.pfe')
camera = Camera()
KeyMapping.setCamera(camera)

# Create window
screen = pygame.display.set_mode((1024, 758))
pygame.display.set_caption('Procedural Generation Viewer')

# Initialization complete, continue with game loop
gameState.advanceCurrentState()
while gameState.getCurrentState() == gameState.GAME_STATE_RUNNING:
    # Reset screen
    screen.fill(colorBlack)

    # Render placeholder GUI
    levelName = font.render('Testlevel', False, colorWhite)
    rectangle = levelName.get_rect()
    screen.blit(levelName, rectangle)

    # Fetch events from pygame and decide what to do with them
    for event in pygame.event.get():
        if event.type == QUIT:
            gameState.advanceCurrentState()
            eventSystem.queueEvent(GameEvent('quit'))
        elif event.type in (KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            KeyMapping.handleInputEvent(event)

    # Render objects of world as static images
    for object in world.objects:
        screen.blit(world.objectImageMapping[object.name], (object.x * TILESIZE - camera.x, object.y * TILESIZE - camera.y))

    # Update display and complete frame
    pygame.display.update()
    deltaTime = clock.tick(FRAMES_PER_SECOND)

# Cleanup before game exits gracefully
pygame.quit()
