import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow

from key_notifier import KeyNotifier
from oliveMovement import OliveMovement
from badzoMovement import BadzoMovement


class SimMoveDemo(QMainWindow):

    def __init__(self):
        super().__init__()

        self.pix1 = QPixmap('images\\Popeye.png')
        self.pix2 = QPixmap('images\\oliveOyl.png')
        self.pix3 = QPixmap('images\\Badzo.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)

        self.hitFloor = False
        self.hitSide = False

        self.hitSide2 = False;
        self.hitFloor2 = False;
        #self.timerP1 = QTimer(self)
        #self.timerP1.setInterval(2000)
        #self.timerP1.setSingleShot(True)

        #self.timerP2 = QTimer(self)
        #self.timerP2.setInterval(2000)
        #self.timerP2.setSingleShot(True)

        self.setWindowState(Qt.WindowMaximized)
        self.__init_ui__()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        self.oliveMovement = OliveMovement()
        self.oliveMovement.oliveMovementSignal.connect(self.moveOlive)
        self.oliveMovement.start()

        self.badzoMovement = BadzoMovement()
        self.badzoMovement.badzoMovementSignal.connect(self.moveBadzo)
        self.badzoMovement.start()

    def __init_ui__(self):

        font = QtGui.QFont()
        font.setPointSize(40)

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(1000, 900, 50, 50)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(50, 50, 50, 50)

        self.label3.setPixmap(self.pix3)
        self.label3.setGeometry(50, 400, 50, 50)

        self.setWindowTitle('Popeye')
        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        rec1 = self.label1.geometry()

        if key == Qt.Key_Right:
            self.label1.setGeometry(rec1.x() + 5, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            self.label1.setGeometry(rec1.x(), rec1.y() + 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            self.label1.setGeometry(rec1.x(), rec1.y() - 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            self.label1.setGeometry(rec1.x() - 5, rec1.y(), rec1.width(), rec1.height())

    def moveOlive(self):
        rec2 = self.label2.geometry()
        if (rec2.x() == 1880):
            self.hitSide = True
        elif (rec2.x() == 0):
            self.hitSide = False

        if self.hitSide:
            self.label2.setGeometry(rec2.x() - 10, rec2.y() + 0, rec2.width(), rec2.height())
        else:
            self.label2.setGeometry(rec2.x()+10, rec2.y() + 0, rec2.width(), rec2.height())

    def moveBadzo(self):
        rec3 = self.label3.geometry()
        if(rec3.x() == 1880):
            self.hitSide2 = True
        elif(rec3.x() == 0):
            self.hitSide2 = False

        if self.hitSide:
            self.label3.setGeometry(rec3.x() - 10, rec3.y() + 0, rec3.width(), rec3.height())
        else:
            self.label3.setGeometry(rec3.x() + 10, rec3.y() + 0, rec3.width(), rec3.height())

    def closeEvent(self, event):
        self.key_notifier.die()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
