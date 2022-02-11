from multiprocessing import Process,Queue
from random import randint
from time import time

def task_handler(curr_list, result_queue):
    total = 0
#    print('in task_handler,curr_list begin is %d.'%curr_list[0])
    for num in curr_list:
        total += num
    result_queue.put(total)
#    print('this list total is %d' %total)
def main():
    start = time()
    process = []
    number_list = [x for x in range(1, 10000001)]
    result_queue = Queue()
    index = 0
    total = 0
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index+1250000], result_queue))
        index += 1250000
        process.append(p)
        p.start()
    for x in process:
        x.join()

    while not result_queue.empty():
        total += result_queue.get()
#        print(total)

    print(total)
    end = time()

    print('use time %.2f sec'% (end-start))

if __name__ == '__main__':
    main()
