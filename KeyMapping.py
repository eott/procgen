from GameEvent import *
from pygame.locals import *
from Movement import *


class KeyMapping:

    keyEventTypeMapping = {
        K_w: GameEvent.MOVE_UP,
        K_s: GameEvent.MOVE_DOWN,
        K_a: GameEvent.MOVE_LEFT,
        K_d: GameEvent.MOVE_RIGHT,
    }

    @staticmethod
    def setMovement(mov):
        KeyMapping.movement = mov

    @staticmethod
    def handleInputEvent(event):
        """Encodes and decides what to do with the given pygame event."""
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
        if event.key in KeyMapping.keyEventTypeMapping:
            move = KeyMapping.keyEventTypeMapping[event.key]
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
        if event.key in KeyMapping.keyEventTypeMapping:
            move = KeyMapping.keyEventTypeMapping[event.key]
            if move == GameEvent.MOVE_UP:
                KeyMapping.movement.subVelocity(Movement.UP)
            elif move == GameEvent.MOVE_DOWN:
                KeyMapping.movement.subVelocity(Movement.DOWN)
            elif move == GameEvent.MOVE_LEFT:
                KeyMapping.movement.subVelocity(Movement.LEFT)
            elif move == GameEvent.MOVE_RIGHT:
                KeyMapping.movement.subVelocity(Movement.RIGHT)

    @staticmethod
    def _mousedownEvent(event):
        pass

    @staticmethod
    def _mouseupEvent(event):
        pass

    @staticmethod
    def _mousemotionEvent(event):
        pass