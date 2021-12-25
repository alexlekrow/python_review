from semaphore import *

if __name__ == '__main__':
    sem = Semaphore(2)
    sem.aquire()
    sem.aquire()
    sem.release()
    sem.release()
