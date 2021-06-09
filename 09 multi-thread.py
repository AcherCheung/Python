# _thread 实现
'''
import _thread
import logging
from time import time, sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2, 4]


def loop(nloop, nsec, lock):
    logging.info('start loop '+ str(nloop) + 'at' + ctime())
    sleep(nsec)
    logging.info('end loop ' + str(nloop) + 'at' + ctime())
    lock.release()


def main():
    logging.info('start all loops ' + 'at' + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked() : pass
    logging.info('end of all ' + 'at' + ctime())


if __name__ == '__main__':
    main()
'''

# threading 实现
'''
import _thread
import logging
import threading
from time import time, sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2, 4]


def loop(nloop, nsec):
    logging.info('start loop ' + str(nloop) + 'at' + ctime())
    sleep(nsec)
    logging.info('end loop ' + str(nloop) + 'at' + ctime())


def main():
    logging.info('start all loops ' + 'at' + ctime())
    thread = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        thread.append(t)
    for i in nloops:
        thread[i].start()
    for i in nloops:
        thread[i].join()
    logging.info('end all loops ' + 'at' + ctime())

    
if __name__ == '__main__':
    main()
'''

# 继承Thread实现--推荐
import _thread
import logging
import threading
from time import time, sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2, 4]


class MyThread(threading.Thread):
    def __init__(self, func, args, name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    logging.info('start loop ' + str(nloop) + 'at' + ctime())
    sleep(nsec)
    logging.info('end loop ' + str(nloop) + 'at' + ctime())


def main():
    logging.info('start all loops ' + 'at' + ctime())
    thread = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        thread.append(t)
    for i in nloops:
        thread[i].start()
    for i in nloops:
        thread[i].join()
    logging.info('end all loops ' + 'at' + ctime())


if __name__ == '__main__':
    main()