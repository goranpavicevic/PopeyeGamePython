import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton


class GameOver(QMainWindow):

    def __init__(self, br):
        super().__init__()

        oImage = QImage("images\\over.jpg")
        self.label = QLabel(self)

        self.who_is_winner = QLabel(self)
        self.who_is_winner1 = QPixmap('images\\player1-wins.png')
        self.who_is_winner2 = QPixmap('images\\player2-wins.png')
        self.left = 400
        self.top = 200
        self.width = 1000
        self.height = 562

        palette = QPalette()
        sImage = oImage.scaled(QSize(1000, 562))
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.__init_ui__(br)

    def __init_ui__(self,br ):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon('Popeye.png'))
        #self.setWindowState(Qt.WindowFullScreen)

        self.setWindowTitle("Menu")
        if(br==1):
            self.who_is_winner.setPixmap(self.who_is_winner1)
            self.who_is_winner.setGeometry(300, 100, 395, 43)
        else:
            self.who_is_winner.setPixmap(self.who_is_winner2)
            self.who_is_winner.setGeometry(300, 100, 395, 43)

        button4 = QPushButton('QUIT', self)
        button4.resize(200, 30)
        button4.move(400, 316)

        button4.clicked.connect(self.quit_on_click)
        self.show()

    def quit_on_click(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameOver()
    sys.exit(app.exec_())