class GameEvent:

    GAME_EVENT_DEFAULT = 1
    MOVE_UP = 2
    MOVE_DOWN = 3
    MOVE_LEFT = 4
    MOVE_RIGHT = 5

    def __init__(self, eventType):
        self.eventType = eventType

    def setEventData(self, data):
        self.eventData = data