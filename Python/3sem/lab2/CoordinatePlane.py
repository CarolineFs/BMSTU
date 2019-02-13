from PyQt5.QtCore import QSize

class CoordinatePlane():

    def __init__(self, size, startPos = "center"):
        self.size = size
        self.start = startPos

    def centerPoint(self):
        if self.start == "center":
            size = (self.size.width() / 2, self.size.height() / 2)
            return size