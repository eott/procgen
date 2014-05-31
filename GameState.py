class GameState:
    """Encapsulates information about the game state."""

    GAME_STATE_INIT = 0
    GAME_STATE_RUNNING = 1
    GAME_STATE_ENDING = 2

    _currentState = GAME_STATE_INIT

    def getCurrentState(self):
        """Returns the game state the game is currently in."""
        return self._currentState

    def advanceCurrentState(self):
        """Advances the game state to the next state. Returns if the change was successful."""
        if self._currentState == self.GAME_STATE_INIT:
            self._currentState = self.GAME_STATE_RUNNING
            return True
        elif self._currentState == self.GAME_STATE_RUNNING:
            self._currentState = self.GAME_STATE_ENDING
            return True
        else:
            return False