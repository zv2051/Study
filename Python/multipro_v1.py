from os import getpid
from multiprocessing import Process
from random import randint
from time import time, sleep

def down_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成，耗时%d.' %(filename, time_to_download))
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=down_task,args=('book A',))
    p2 = Process(target=down_task, args=('book B',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗时%2fsec' %(end-start))
    

if __name__ == '__main__':
    main()

