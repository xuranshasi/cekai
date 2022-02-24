# 标准库
# import os

# print(os.getcwd())

# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     with open("b/test.txt","w") as f:
#         f.write("os, i am coming")


# import  time

# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# import urllib.request
#
# response = urllib.request.urlopen("https://wwww.baidu.com")
# print(response.status)
# print(response.read())


# import math
#
# print(math.ceil(5.3))
# print(math.floor(5.9))
#
# print(math.sqrt(16))


# 线程
import _thread
import logging
import threading
from time import ctime, sleep

from cffi.cparser import lock

logging.basicConfig(level=logging.INFO)

# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#     logging.info("end loop0 at " + ctime())
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)
#     logging.info("end loop1 at " +ctime())

loops = [2, 4, 2, 2, 2, 2]


# def loop(nloops, nsec, lock):
#     logging.info("start loop" + str(nloops) + " at " + ctime())
#     sleep(nsec)
#     logging.info("end loop" + str(nloops) + " at " + ctime())
#     lock.release()


# def main():
#     logging.info("stat all at " + ctime())
#     locks = []
#     nploops = range(len(loops))
#     for i in nploops:
#         lock = _thread.allocate_lock()
#         lock.acquire()
#         locks.append(lock)
#
#     for i in nploops:
#         _thread.start_new_thread(loop, (i, loops[i], locks[i]))
#
#     for i in nploops:
#         while locks[i].locked(): pass
#
#     # _thread.start_new_thread(loop0, ())
#     # _thread.start_new_thread(loop1, ())
#     # sleep(6)
#     logging.info("end all at " + ctime())


# def loop(nloops, nsec):
#     logging.info("start loop" + str(nloops) + " at " + ctime())
#     sleep(nsec)
#     logging.info("end loop" + str(nloops) + " at " + ctime())
#
#
# def main():
#     logging.info("stat all at " + ctime())
#     threads = []
#     nploops = range(len(loops))
#
#     for i in nploops:
#         t = threading.Thread(target=loop, args=(i, loops[i]))
#         threads.append(t)
#     for i in nploops:
#         threads[i].start()
#     for i in nploops:
#         threads[i].join()
#     logging.info("end all at " + ctime())

class Mythread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloops, nsec):
    logging.info("start loop" + str(nloops) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloops) + " at " + ctime())


def main():
    logging.info("stat all at " + ctime())
    threads = []
    nploops = range(len(loops))

    for i in nploops:
        t = Mythread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nploops:
        threads[i].start()
    for i in nploops:
        threads[i].join()
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
