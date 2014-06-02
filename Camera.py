class Camera:

    ZOOM_STEP = 0.25

    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom = 1.0
        self.speed = 50  # pixel, not tiles
        self._width = 15  # tiles, not pixel
        self._height = 9  # tiles, not pixel

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def moveBy(self, x, y):
        self.x += x
        self.y += y

    def incZoom(self):
        self.zoom += Camera.ZOOM_STEP

    def decZoom(self):
        self.zoom -= Camera.ZOOM_STEP

    def getWidth(self):
        return (self._width * self.zoom).ceil()

    def getHeight(self):
        return (self._height * self.zoom).ceil()