from threading import Thread
from time import sleep

class Account(object):
    def __init__(self):
        self._blance = 0

    def deposit(self, money):
        print('in _deposit')
        new_blance = self._blance + money
        sleep(0.1)
        self._blance = new_blance
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
