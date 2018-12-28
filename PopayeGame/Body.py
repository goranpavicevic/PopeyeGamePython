from PyQt5.QtWidgets import QLabel

from TextureLoader import TextureLoader


class Body:

    POPEYE = None
    OLIVEOYL = None
    BADZO = None

    name = ""
    texture = "unknown"

    def __init__(self, name, texture):
        self.name = name
        self.texture = texture

    def construct_widget(self, window):
        label = QLabel(window)

        texture = TextureLoader.textures[self.texture]

        label.setPixmap(texture)
        label.resize(texture.width(), texture.height())

        return label


Body.POPEYE = Body("Popeye", "popeye")
Body.OLIVEOYL = Body("OliveOyl", "oliveoyl")


