import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton
from sim_move_demo import SimMoveDemo
from PyQt5.QtCore import Qt

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        oImage = QImage("images\\MenuPicture.png")


        self.label = QLabel(self)

        self.left = 400
        self.top = 200
        self.width = 1000
        self.height = 562

        palette = QPalette()
        sImage = oImage.scaled(QSize(1000, 562))
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.__init_ui__()

    def __init_ui__(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon('Popeye.png'))
        # self.setWindowState(Qt.WindowFullScreen)

        self.setWindowTitle("Menu")

        button1 = QPushButton('1 PLAYER GAME', self)
        button1.resize(400, 43)
        button1.move(300, 210)
        button1.clicked.connect(self.one_players_on_click)

        button2 = QPushButton('2 PLAYER GAME', self)
        button2.resize(400, 43)
        button2.move(300, 253)
        button2.clicked.connect(self.two_players_on_click)


        button4 = QPushButton('QUIT', self)
        button4.resize(330, 43)
        button4.move(330, 316)

        button4.clicked.connect(self.quit_on_click)
        self.show()


    def one_players_on_click(self):
        self.one = SimMoveDemo()
        self.one.show()

    def two_players_on_click(self):
        self.two = SimMoveDemo()
        self.two.show()

    def quit_on_click(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())
