from multiprocessing import Process
from multiprocessing import Queue
from time import sleep


def sub_task(str1, flag):
    while True:
        i= flag.get(True)
        flag.put(i+1)
        print(str1+(str(i)), end='\n', flush=True)
        sleep(0.1)
        if i>=8:
            break
def main():
    flagg = Queue()
    flagg.put(0)
    p1 = Process(target=sub_task, args=('ping',flagg))
    p2 = Process(target=sub_task, args=('pong',flagg))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    main()
