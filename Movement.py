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
        self.puppet = puppet

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

    def doMovement(self):
        self.puppet.moveBy(self.getVeloX(), self.getVeloY())