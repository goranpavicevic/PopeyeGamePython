from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QLabel

from TextureLoader import TextureLoader


class ControlableObject(QObject):
    # DIRECTION_LEFT = 1
    # DIRECTION_RIGHT = 3
    # DIRECTION_UP = 5
    # DIRECTION_DOWN = 2

    name = ""
    texture = ""
    speed = 50

    label = None
    window = None
    signal_move_frogger = pyqtSignal(object, int, int)

    def __init__(self, window, name, texture):
        super().__init__()
        self.name = name
        self.texture = texture
        self.window = window

        self.label = QLabel(window)

        texture = TextureLoader.textures[self.texture]

        self.label.setPixmap(texture)
        self.label.resize(texture.width(), texture.height())

    def move_frogger(self, key):
        position = self.label.pos()

        x = position.x()
        y = position.y()

        if key == Qt.Key_Right and x + self.speed <= 50 * 14:
            self.label.move(x + self.speed, y)
        elif key == Qt.Key_Down and y + self.speed <= 50 * 14:
            self.label.move(x, y + self.speed)
        elif key == Qt.Key_Up and y - self.speed >= 50:
            self.label.move(x, y - self.speed)
        elif key == Qt.Key_Left and x - self.speed >= 0:
            self.label.move(x - self.speed, y)

    def check_collision(self, moving_object):
        pos1 = self.label.pos()
        pos2 = moving_object.label.pos()

        x1 = pos1.x()
        y1 = pos1.y()

        x2 = pos2.x()
        y2 = pos2.y()

        if x1 < x2 + 50 and x1 + 50 > x2 and y1 < y2 + 50 and y1 + 50 > y2:
            return True
        return False



