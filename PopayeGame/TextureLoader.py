from PyQt5.QtGui import QPixmap

class TextureLoader:

    texture_names = ["popeye", "oliveOyl", "badzo"
                     ]

    textures = {}

    @staticmethod
    def load():
        for x in TextureLoader.texture_names:
            pixmap = QPixmap("images/" + x + ".png")
            TextureLoader.textures[x] = pixmap