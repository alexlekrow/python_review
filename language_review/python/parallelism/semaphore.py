from threading import Condition, Lock, Thread


class Semaphore(object):
    def __init__(self, max_available):
        self.cv = threading.Condition()
        self.MAX_AVAILABLE = max_available
        self.taken = 0

    def aquire(self):
        self.cv.aquire()
        while (self.taken == self.MAX_AVAILABLE):
            self.cv.wait()
        self.taken += 1
        self.cv.release()

    def release(self):
        self.cv.aquire()
        self.taken -= 1
        self.cv.notify()
        self.cv.release()
