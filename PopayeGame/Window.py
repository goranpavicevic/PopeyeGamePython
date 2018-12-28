import random

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel

from ControlableObject import ControlableObject
from Movement import Movement
from TextureLoader import TextureLoader
from GameThread import GameThread
from Body import Body
from Score import Score


class Window(QMainWindow):

    game_map = []
    moving_objects = []
    ticking_thread = None

    tile_size = 50
    signal_end = None

    player1info = None
    player2info = None

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Popeye")
        self.setWindowIcon(QIcon("Popeye.png"))
        self.setGeometry(100, 100, 15 * self.tile_size, 16 * self.tile_size)
        self.setFixedSize(self.size())

        self.setWindowIcon(QIcon("oliveOyl.png"))
        self.setGeometry(1000, 250, 15 * self.tile_size, 16 * self.tile_size)
        self.setFixedSize(self.size())

        self.player1info = Score()
        self.player2info = Score()

        TextureLoader.load()
#        self.init_map()
#        self.draw_map()
        self.init_frogger()
        self.init_olive_oyl()

    #    self.start_ticking()

    def move_object(self, obj, x, y):
        obj.move(x, y)

    def add_moving_object(self, name, texture, position, speed, direction, lane):
        obj = Movement(self, name, texture, speed, direction)
        obj.signal_move.connect(self.move_object)
        obj.label.move(position * self.tile_size, lane * self.tile_size)
        obj.label.show()

        self.moving_objects.append(obj)

    def add_new_car(self):
        lane = random.randint(9, 13)
        self.add_moving_object("Car", "car1", -1, 5, Movement.DIRECTION_RIGHT, lane)
        self.add_new_tree()

    def add_new_tree(self):
        lane = random.randint(3,7)
        self.add_moving_object("Tree","tree_medium", 15, 5, Movement.DIRECTION_LEFT, lane)

    def move_end(self, object):
        #Called from ticking thread
        object.label.clear()
        object.label.destroy()
        self.moving_objects.remove(object)

  #  def init_map(self):
  #     self.game_map.append([Body.GRASS2, Body.GRASS3, Body.GRASS4] * 5)

    def car_hit(self):
        self.frogger.label.move(self.tile_size * 7, self.tile_size * 14)
        self.player1info.lives()

    def draw_map(self):
        columns = len(self.game_map)
        rows = len(self.game_map[0])

        for x in range(columns):
            for y in range(rows):
                img = self.game_map[x][y].construct_widget(self)
                img.move(y * self.tile_size, (1 + x) * self.tile_size)

    def keyPressEvent(self, event):
        self.frogger.move_frogger(event.key())
        self.frogger.label.show()

    def init_frogger(self):
        self.frogger = ControlableObject(self, "Popeye", "popeye")
        self.frogger.label.move(self.tile_size * 7, self.tile_size * 14)

    def init_olive_oyl(self):
        self.frogger = ControlableObject(self, "oliveOyl", "oliveoyl")
        self.frogger.label.move(self.tile_size * 7, self.tile_size * 14)

    def start_ticking(self):
        self.ticking_thread = GameThread(self)
        self.ticking_thread.signal_add_car.connect(self.add_new_car)
        self.ticking_thread.signal_car_hit.connect(self.car_hit)
        self.ticking_thread.start()

    def stop_ticking(self):
        self.ticking_thread.stop()

    def closeEvent(self, *args, **kwargs):
        self.stop_ticking()