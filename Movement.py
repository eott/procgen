class Movement:

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    _standardSpeed = 2.5

    def __init__(self):
        self.speedX = 0
        self.speedY = 0

    def setPuppet(self, puppet):
        """Sets the object, that is controlled by the movement object, to the given value. The puppet must implement
           a moveBy(x, y) and moveTo(x, y) method, that moves the object by or to the given coordinates."""
        self.puppet = puppet

    def addVelocity(self, direction):
        """Adds the given velocity to the overall velocity of the puppet. The parameter must have a the x in the first
           and the y component in the second position. The velocity is assumed to be in units of standard speed, not
           pixels."""
        self.speedX += direction[0]
        self.speedY += direction[1]

    def subVelocity(self, direction):
        """Subtracts the given velocity from the overall velocity of the puppet. The parameter must have a the x in the
           first and the y component in the second position. The velocity is assumed to be in units of standard speed,
           not pixels."""
        self.speedX -= direction[0]
        self.speedY -= direction[1]

    def getVeloX(self):
        return self._standardSpeed * self.speedX

    def getVeloY(self):
        return self._standardSpeed * self.speedY

    def doMovement(self):
        """Should be called every frame and applies the movement information to the puppet object."""
        self.puppet.moveBy(self.getVeloX(), self.getVeloY())