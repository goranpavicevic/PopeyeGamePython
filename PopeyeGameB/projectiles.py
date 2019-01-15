import time
from random import randint

def isHit(first, second):
    rec1 = first.geometry()
    y1 = first.height()
    x1 = first.width()
    rec2 = second.geometry()
    x2 = second.width()
    y2 = second.height()
    if rec1.x() + x1 in range(rec2.x(), rec2.x() + x2):
        if rec1.y() in range(rec2.y(), rec2.y() + y2):
            return True
        elif rec1.y() + y1 in range(rec2.y(), rec2.y() + y2):
            return True

    if rec1.x() in range(rec2.x(), rec2.x() + x2):
        if rec1.y() in range(rec2.y(), rec2.y() + y2):
            return True
        elif rec1.y() + y1 in range(rec2.y(), rec2.y() + y2):
            return True

    if rec2.x() + x2 in range(rec1.x(), rec1.x() + x1):
        if rec2.y() in range(rec1.y(), rec1.y() + y1):
            return True
        elif rec2.y() + y2 in range(rec1.y(), rec1.y() + y1):
            return True

    if rec2.x() in range(rec1.x(), rec1.x() + x1):
        if rec2.y() in range(rec1.y(), rec1.y() + y1):
            return True
        elif rec2.y() + y2 in range(rec1.y(), rec1.y() + y1):
            return True


def force(q):
    while True:
        time.sleep(randint(15, 20))
        for i in range(15):
            q.put(randint(100, 1820))
            time.sleep(0.5)


def jump(q):
    while True:
        time.sleep((randint(8, 12)))
        q.put(1)


def generateBottles(q):
    while True:
        time.sleep(randint(10, 17))
        for i in range(4):
            q.put(1)
            time.sleep(1)


def BadzoFreezeProcess(start, stop):
    while True:
        a = stop.get()
        time.sleep(5)
        start.put(1)
