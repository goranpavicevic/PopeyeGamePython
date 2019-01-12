from PyQt5.QtCore import QThread,QObject,pyqtSignal,pyqtSlot
from random import randint
import time


class BombsMovement(QObject):
    bombsMovementSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.thread = QThread()
        # move the Worker object to the Thread object
        # "push" self from the current thread to this thread
        self.moveToThread(self.thread)
        # Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.__work__)

    def start(self):
        """
        Start notifications.
        """
        self.thread.start()

    def die(self):
        """
        End notifications.
        """
        self.thread.quit()

    @pyqtSlot()
    def __work__(self):
        """
        A slot with no params.
        """
        while True:
            self.bombsMovementSignal.emit()
            time.sleep(0.08)


def force(q):
    while True:
        time.sleep(randint(15, 20))
        for i in range(15):
            q.put(randint(100, 1820))
            time.sleep(0.4)

