from GameEvent import *
from pygame.locals import *
from Movement import *


class KeyMapping:

    keyEventTypeMapping = {
        'w': GameEvent.MOVE_UP,
        's': GameEvent.MOVE_DOWN,
        'a': GameEvent.MOVE_LEFT,
        'd': GameEvent.MOVE_RIGHT,
    }

    @staticmethod
    def setMovement(mov):
        KeyMapping.movement = mov

    @staticmethod
    def handleInputEvent(event):
        if event.type == KEYDOWN:
            KeyMapping._keydownEvent(event)
        elif event.type == KEYUP:
            KeyMapping._keyupEvent(event)
        elif event.type == MOUSEBUTTONDOWN:
            KeyMapping._mousedownEvent(event)
        elif event.type == MOUSEBUTTONUP:
            KeyMapping._mouseupEvent(event)
        elif event.type == MOUSEMOTION:
            KeyMapping._mousemotionEvent(event)

    @staticmethod
    def _keydownEvent(event):
        if event.unicode in KeyMapping.keyEventTypeMapping:
            move = KeyMapping.keyEventTypeMapping[event.unicode]
            if move == GameEvent.MOVE_UP:
                KeyMapping.movement.addVelocity(Movement.UP)
            elif move == GameEvent.MOVE_DOWN:
                KeyMapping.movement.addVelocity(Movement.DOWN)
            elif move == GameEvent.MOVE_LEFT:
                KeyMapping.movement.addVelocity(Movement.LEFT)
            elif move == GameEvent.MOVE_RIGHT:
                KeyMapping.movement.addVelocity(Movement.RIGHT)

    @staticmethod
    def _keyupEvent(event):
        pass

    @staticmethod
    def _mousedownEvent(event):
        pass

    @staticmethod
    def _mouseupEvent(event):
        pass

    @staticmethod
    def _mousemotionEvent(event):
        pass