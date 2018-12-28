from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QLabel

from TextureLoader import TextureLoader


class Movement(QObject):

    DIRECTION_LEFT = -1
    DIRECTION_RIGHT = 1

    name = ""
    texture = ""
    speed = 1
    direction = DIRECTION_LEFT

    label = None
    window = None
    signal_move = pyqtSignal(object, int, int)

    def __init__(self, window, name, texture, speed, direction):
        super().__init__()
        self.name = name
        self.texture = texture
        self.speed = speed
        self.direction = direction
        self.window = window

        self.label = QLabel(window)

        texture = TextureLoader.textures[self.texture]

        self.label.setPixmap(texture)
        self.label.resize(texture.width(), texture.height())

    def move(self):
        position = self.label.pos()

        x = position.x() + self.direction * self.speed

        if x >= 50 * 15 or x <= 50 * -1:
            self.die()
            return

        self.signal_move.emit(self.label, x, position.y())
        #self.label.move(x, position.y())

    def die(self):
        self.window.move_end(self)