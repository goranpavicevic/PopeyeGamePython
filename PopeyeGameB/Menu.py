import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton
from sim_move_demo import SimMoveDemo
from PyQt5.QtCore import Qt

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        oImage = QImage("images\\MenuPicture.png")

        self.label = QLabel(self)
        self.label1Player = QLabel(self)
        self.oneplayer = QPixmap('images\\JedanIgrac.png')

        self.label2Player = QLabel(self)
        self.twoplayer = QPixmap('images\\DvaIgraca.png')

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

        #RESENJE 1 : SA BUTTON-IMA
        #button1 = QPushButton('1 PLAYER GAME', self)
        #button1.resize(400, 43)
        #button1.move(300, 210)
        #button1.clicked.connect(self.one_players_on_click)

        #button2 = QPushButton('2 PLAYER GAME', self)
        #button2.resize(400, 43)
        #button2.move(300, 253)
        #button2.clicked.connect(self.two_players_on_click)

        button4 = QPushButton('QUIT', self)
        button4.resize(330, 43)
        button4.move(330, 316)

        button4.clicked.connect(self.quit_on_click)

        #RESENJE 2 : SA LABELAMA
        self.label1Player.setPixmap(self.oneplayer)
        self.label1Player.setGeometry(300, 210, 395, 43)
        self.label1Player.mousePressEvent = self.one_players_on_click

        self.label2Player.setPixmap(self.twoplayer)
        self.label2Player.setGeometry(300, 263, 395, 43)
        self.label2Player.mousePressEvent = self.two_players_on_click

        self.show()

    def one_players_on_click(self,event):
        self.one = SimMoveDemo(1, 1)
        self.one.show()
        self.hide()

    def two_players_on_click(self,event):
        self.two = SimMoveDemo(2, 1)
        self.two.show()
        self.hide()

    def quit_on_click(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())
