from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip, QDesktopWidget
from PyQt5.QtGui import QFont, QPainter
from CoordinatePlane import *
from PyQt5.QtCore import Qt
from Astroid import *
from Figure import *

class Mainframe(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # QToolTip.setFont(QFont('SansSerif', 10))

        # self.setToolTip('This is a <i><b>QWidget</b></i> widget')

        btn = QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        sizeScreen = QDesktopWidget().availableGeometry()

        self.setGeometry(0, 0, sizeScreen.width(), sizeScreen.height())
        # self.drawPlane()
        self.setWindowTitle('Lab 2')
        self.show()

    def paintEvent(self, e):
        self.drawPlane()

    def drawPlane(self):
        self.coordinatePlane = CoordinatePlane(self.size())
        center = self.coordinatePlane.centerPoint()
        figures = []
        figures.append(Astroid())
        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.red)
        qp.drawPoint(center[0], center[1])

        for i in figures:
            path = i.draw()
            qp.drawLine(path[0], path[1], path[2], path[3])

        qp.drawLine(center[0],0,center[0], self.size().height())
        qp.drawLine(0, center[1], self.size().width(), center[1])
        qp.end()