from PyQt5.QtCore import QThread,QObject,pyqtSignal,pyqtSlot
from random import randint

import time


def force(q):
    a = 0
    while True:
        a += 1
        if a > 20:
            b = randint()
            if b % 13 == 0:
                q.put(randint(100, 1800))
        time.sleep(1)
