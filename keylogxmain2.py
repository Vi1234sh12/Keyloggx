
from PySide2 import QtCore , QtGui , QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication

import main

class  MainWindow(QMainWindow):
    def  __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)


        self.show()





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = FIRST_WINDOW_CLASS()
    sys.exit(app.exec_())

