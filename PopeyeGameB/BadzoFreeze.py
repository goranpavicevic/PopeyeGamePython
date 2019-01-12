from multiprocessing import Queue
import time


def BadzoFreezeProcess(start, stop):
    while True:
        if not stop.empty():
            a = stop.get()
            time.sleep(5)
            start.put(1)