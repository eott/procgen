from GameEvent import *
from pygame.locals import *


class KeyMapping:

    keyEventTypeMapping = {
        'w': GameEvent.MOVE_UP,
        's': GameEvent.MOVE_DOWN,
        'a': GameEvent.MOVE_LEFT,
        'd': GameEvent.MOVE_RIGHT,
    }

    @staticmethod
    def setCamera(cam):
        KeyMapping.camera = cam

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
                KeyMapping.camera.moveBy(0, -KeyMapping.camera.speed)
            elif move == GameEvent.MOVE_DOWN:
                KeyMapping.camera.moveBy(0, KeyMapping.camera.speed)
            elif move == GameEvent.MOVE_LEFT:
                KeyMapping.camera.moveBy(-KeyMapping.camera.speed, 0)
            elif move == GameEvent.MOVE_RIGHT:
                KeyMapping.camera.moveBy(KeyMapping.camera.speed, 0)

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