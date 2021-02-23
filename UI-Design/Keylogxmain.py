from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import QPropertyAnimation, QPoint, QTime, QDateTime, QObject, QTimerEvent, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect, QPushButton, QComboBox, QHBoxLayout, QProgressBar
import sys
import main


counters = 0 

class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow  ):
    def __init__(self, parent=None):
        super( MainWindow, self).__init__(parent)
        self.setupUi(self)

        #remove titile bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(5)
        self.shadow.setXOffset(3)
        self.shadow.setYOffset(3)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        #Qtimer --> start 
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)


def progress(self):
    global counter

    self.ui.progressBar.setValue(counter)

    if counter > 100 :

        self.timer.stop()

        self.close()

     
            

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
