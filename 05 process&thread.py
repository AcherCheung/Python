
# 单进程
'''
import random
import time

def download_task(filename):
    print(f'{filename}开始下载')
    time_to_download = random.randint(3, 6)
    time.sleep(time_to_download)
    print(f'{filename}下载完毕,共花费了%.2f秒' % time_to_download)



def main():
    start = time.time()
    download_task('七个小矮人')
    download_task('阿里巴巴与四十大盗')
    end = time.time()
    print('共花费了%.2f秒' % (end-start))

if __name__ == '__main__':
    main()
'''

# 多进程

'''
from multiprocessing import Process
from os import getpid
from random import randint
from time import sleep,time


def download_task(filename):
    print('启动下载进程……，进程号%d' % getpid())
    print(f'{filename}开始下载')
    time_to_download = randint(3, 6)
    sleep(time_to_download)
    print(f'{filename}下载完毕,共花费了%.2f秒' % time_to_download, end='\n')



def main():
    start = time()
    p1 = Process(target=download_task, args=('七个小矮人',))
    p1.start()
    p2 = Process(target=download_task, args=('阿里巴巴与四十大盗',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('共花费了%.2f秒' % (end-start))


if __name__ == '__main__':
    main()
'''

# 多线程
'''
from threading import Thread
from os import getpid
from random import randint
from time import sleep,time


def download_task(filename):
    print('启动下载进程……，进程号%d' % getpid())
    print(f'{filename}开始下载')
    time_to_download = randint(3, 6)
    sleep(time_to_download)
    print(f'{filename}下载完毕,共花费了%.2f秒' % time_to_download, end='\n')


def main():
    start = time()
    p1 = Thread(target=download_task, args=('七个小矮人',))
    p1.start()
    p2 = Thread(target=download_task, args=('阿里巴巴与四十大盗',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('共花费了%.2f秒' % (end-start))


if __name__ == '__main__':
    main()
'''

# 通过"继承"Thread类实现多线程
'''
from threading import Thread
from os import getpid
from random import randint
from time import sleep,time


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        print('启动下载进程……，进程号%d' % getpid())
        print(f'{self.filename}开始下载')
        time_to_download = randint(3, 6)
        sleep(time_to_download)
        print(f'{self.filename}下载完毕,共花费了%.2f秒' % time_to_download, end='\n')


def main():
    start = time()
    p1 = DownloadTask('七个小矮人')
    p1.start()
    p2 = DownloadTask('阿里巴巴与四十大盗')
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('共花费了%.2f秒' % (end-start))


if __name__ == '__main__':
    main()
'''

# 线程不加锁，100个线程同时向一个账户转账
'''
from time import sleep
from threading import Thread


class Account():
    def __init__(self):
        self._balance = 0

    def deposite(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟执行的时间
        sleep(0.005)
        # 更新账户余额
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposite(self._money)


class main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为%.2f' % account.balance)


if __name__ == '__main__':
    main()
#     输出为5，大大小于100，
#     多个线程同时向账户中存钱时，会一起执行到new_balance = self._balance + money这行代码，
#     多个线程得到的账户余额都是初始状态下的0，所以都是0上面做了+1的操作，因此得到了错误的结果
'''

# 线程锁，多线程
'''
from time import sleep
from threading import Thread, Lock


class Account():
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposite(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟执行的时间
            sleep(0.005)
            # 更新账户余额
            self._balance = new_balance
        # 在finally中执行释放锁的操作保证正常异常锁都能释放
        finally:
            self._lock.release()


    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposite(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
'''

# 单进程计算
'''
from time import time


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()
'''
from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()