from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs = []
    try:
        for fn in filenames:
            fs.append(open(fn,'w',encoding = 'utf-8'))
        for num in range(1,10000):
            if is_prime(num):
                if num < 100:
                    fs[0].write(str(num) + '\n')
                elif num < 1000:
                    fs[1].write(str(num) + '\n')
                else:
                    fs[2].write(str(num) + '\n')
    except IOError as ex:
        print(ex)
    finally:
        for f in fs:
            f.close()

if __name__=='__main__':
    main()
                        
                
