from threading import Thread
from random import randint
from time import time, sleep

def download(filename):
    print("begin download %s" % filename)
    use_time = randint(5, 10)
    sleep(use_time)
    print('download %s finish,use %d sec' %(filename, use_time))

def main():
    print('123')
    start = time()
    t1 = Thread(target=download, args=('A Book',))
    t1.start()
    t2 = Thread(target=download, args=('B Book',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('two thread use %.2f sec' % (end-start))
if __name__ == '__main__':
    main()
