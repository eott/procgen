from GameEvent import *
from pygame.locals import *


class KeyMapping:

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
        pass

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