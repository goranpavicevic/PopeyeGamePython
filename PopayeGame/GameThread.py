import time

from PyQt5.QtCore import QThread, pyqtSignal


class GameThread(QThread):

    window = None
    should_stop = False
#    signal_add_car = pyqtSignal()
#   signal_car_hit = pyqtSignal()

    def __init__(self, window):
        super().__init__()
        self.window = window

    def run(self):
        tick_num = 0

        while not self.should_stop:
            for obj in self.window.moving_objects:
                obj.move()
                if self.window.frogger.check_collision(obj):
                    #print("Hit")
                    self.signal_car_hit.emit()

            if tick_num % 30 == 0:
                self.signal_add_car.emit()

            tick_num += 1

            time.sleep(20.0 / 1000.0)

    def stop(self):
        self.should_stop = True
