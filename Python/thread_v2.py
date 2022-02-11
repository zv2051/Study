from threading import Thread
from random import randint
from time import time, sleep

class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        print('begin download %s ...' % self.filename)
        use_time = randint(5, 10)
        sleep(use_time)
        print('download %s use %d sec.'% (self.filename, use_time))
def main():
    start = time()
    t1 = DownloadTask("A book")
    t1.start()
    t2 = DownloadTask("B book")
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('total use time %.2f sec.'%(end-start)) 

if __name__ == '__main__':
    main()
