class Movement:

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    _standardSpeed = 2.5

    def addVelocity(self, direction):
        self.speedX += direction[0]
        self.speedY += direction[1]

    def subVelocity(self, direction):
        self.speedX -= direction[0]
        self.speedY -= direction[1]

    def getVeloX(self):
        return self._standardSpeed * self.speedX

    def getVeloY(self):
        return self._standardSpeed * self.speedY