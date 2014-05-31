class EventSystem:
    """Handles the distribution of events across the subsystems of the overall game.
       Classes can attach themselves to specific events with a callback provided,
       which will be called when the corresponding event has occurred."""

    _eventQueue = []
    _eventListener = {}

    def attachListener(self, eventType, listener):
        if len(EventSystem._eventListener[eventType]) == 0:
            EventSystem._eventListener[eventType] = {listener}
        else:
            EventSystem._eventListener[eventType].append(listener)

    def queueEvent(self, event):
        EventSystem._eventQueue.append(event)

    def processEvents(self):
        for event in EventSystem._eventQueue:
            for listener in EventSystem._eventListener[event.eventType]:
                listener.triggerEvent(event)
        EventSystem._eventQueue = []