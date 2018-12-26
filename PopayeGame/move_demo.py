import sys
import  key_notifier

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QApplication



class MoveDemo(QWidget):

    def __init__(self):
        super().__init__()

        oImage = QImage("backround.png")
        sImage = oImage.scaled(QSize(1900, 1080))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        pix11 = QPixmap('Popeye.png')
        pix22 = QPixmap('oliveOyl.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)

        self.pix1 = pix11.scaledToHeight(48)
        self.pix1 = pix11.scaledToWidth(48)

        self.pix2 = pix22.scaledToHeight(48)
        self.pix2 = pix22.scaledToWidth(48)

        self.setWindowState(Qt.WindowFullScreen)

        self.__init_ui__()

    def __init_ui__(self):

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(100, 40, 50, 50)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(50, 40, 50, 50)

        self.setWindowTitle('Slide')
        self.show()

    def keyPressEvent(self, event):
        self.__update_position__(event.key())

    def __update_position__(self, key):
        rec1 = self.label1.geometry()
        rec2 = self.label2.geometry()

        if key == Qt.Key_Right:
            self.label1.setGeometry(rec1.x() + 5, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            self.label1.setGeometry(rec1.x(), rec1.y() + 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            self.label1.setGeometry(rec1.x(), rec1.y() - 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            self.label1.setGeometry(rec1.x() - 5, rec1.y(), rec1.width(), rec1.height())

        if key == Qt.Key_D:
            self.label2.setGeometry(rec2.x() + 5, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_S:
            self.label2.setGeometry(rec2.x(), rec2.y() + 5, rec2.width(), rec2.height())
        elif key == Qt.Key_W:
            self.label2.setGeometry(rec2.x(), rec2.y() - 5, rec2.width(), rec2.height())
        elif key == Qt.Key_A:
            self.label2.setGeometry(rec2.x() - 5, rec2.y(), rec2.width(), rec2.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MoveDemo()
    sys.exit(app.exec_())
