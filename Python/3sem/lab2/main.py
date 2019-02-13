import sys
from Mainframe import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if  __name__ == '__main__':

    app = QApplication(sys.argv)

    w = Mainframe()
    sys.exit(app.exec())