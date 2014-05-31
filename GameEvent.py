class GameEvent:

    GAME_EVENT_DEFAULT = 1

    def __init__(self, eventType):
        self.eventType = eventType

    def setEventData(self, data):
        self.eventData = data