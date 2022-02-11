from threading import Thread, Lock
from time import sleep

class Account(object):
    def __init__(self):
        self._blance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_blance = self._blance + money
            sleep(0.1)
            self._blance = new_blance
        finally:
            self._lock.release()
    @property
    def blance(self):
        return self._blance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    acc = Account()
    threads = []
    for _ in range(100):
        t=AddMoneyThread(acc, 1)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print('total accout blance is %d.'% acc.blance)

if __name__ == '__main__':
    main()
