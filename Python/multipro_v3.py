from time import time
def main():
    start = time()
    total = 0
    for i in range(1, 10000001):
        total += i
    end = time()
    print(total)
    print('use time %.2f sec' %(end-start))

if __name__ == '__main__':
    main()
